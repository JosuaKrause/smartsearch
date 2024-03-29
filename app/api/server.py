# pylint: disable=unused-argument
import sys
import threading
import uuid

from quick_server import create_server, PreventDefaultResponse, QuickServer
from quick_server import QuickServerRequestHandler as QSRH
from quick_server import ReqArgs

from app.api.response_types import (
    SourceListResponse,
    SourceResponse,
    VersionResponse,
)
from app.misc.env import envload_int, envload_str
from app.misc.version import get_version
from app.system.config import get_config
from app.system.db.db import DBConnector
from app.system.jwt import is_valid_token
from app.system.language.pipeline import extract_language
from app.system.language.spacy import LangResponse
from app.system.location.pipeline import extract_locations
from app.system.location.response import GeoOutput, GeoQuery
from app.system.ops.ops import get_ops


MAX_RESPONSE = 1024 * 100  # 100kB  # rough size
MAX_INPUT_LENGTH = 1024 * 1024 * 10  # 10MB
MAX_LINKS = 20


def setup(
        addr: str,
        port: int,
        parallel: bool,
        deploy: bool) -> tuple[QuickServer, str]:
    server: QuickServer = create_server(
        (addr, port),
        parallel,
        thread_factory=threading.Thread,
        token_handler=None,
        worker_constructor=None,
        soft_worker_death=True)

    prefix = "/api"

    server.suppress_noise = True

    def report_slow_requests(method_str: str, path: str) -> None:
        print(f"slow request {method_str} {path}")

    max_upload = 20 * 1024 * 1024 * 1024  # 20GiB
    server_timeout = 10 * 60
    server.report_slow_requests = report_slow_requests
    server.max_file_size = max_upload
    server.max_chunk_size = max_upload
    server.timeout = server_timeout
    server.socket.settimeout(server_timeout)

    if deploy:
        server.no_command_loop = True

    py_version_detail = f"{sys.version}"
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    version_name = get_version(return_hash=False)
    version_hash = get_version(return_hash=True)
    print(f"python version: {py_version_detail}")
    print(f"app version: {version_name}")
    print(f"app commit: {version_hash}")

    server.set_default_token_expiration(48 * 60 * 60)  # 2 days

    config = get_config()
    db = DBConnector(config["db"])
    ops = get_ops("db", config)

    def verify_token(token: str) -> uuid.UUID:
        user = is_valid_token(config, token)
        if user is None:
            raise PreventDefaultResponse(401, "invalid token provided")
        return user

    def verify_input(text: str) -> str:
        if len(text) > MAX_INPUT_LENGTH:
            raise PreventDefaultResponse(
                413, f"input length exceeds {MAX_INPUT_LENGTH} bytes")
        return text

    # *** misc ***

    @server.json_get(f"{prefix}/version")
    def _get_version(_req: QSRH, _rargs: ReqArgs) -> VersionResponse:
        return {
            "app_name": version_name,
            "app_commit": version_hash,
            "python": py_version,
        }

    # *** sources ***

    @server.json_post(f"{prefix}/source")
    def _post_source(_req: QSRH, rargs: ReqArgs) -> SourceResponse:
        args = rargs["post"]
        source = f"{args['source']}"
        ops.add_source(source)
        return {
            "source": source,
        }

    @server.json_get(f"{prefix}/source")
    def _get_source(_req: QSRH, _rargs: ReqArgs) -> SourceListResponse:
        return {
            "sources": ops.get_sources(),
        }

    # *** location ***

    @server.json_post(f"{prefix}/locations")
    def _post_locations(_req: QSRH, rargs: ReqArgs) -> GeoOutput:
        args = rargs["post"]
        input_str = verify_input(args["input"])
        user = verify_token(args["token"])
        obj: GeoQuery = {
            "input": input_str,
            "return_input": args.get("return_input", False),
            "return_context": args.get("return_context", True),
            "strategy": args.get("strategy", "top"),
            "language": args.get("language", "en"),
        }
        return extract_locations(db, obj, user)

    # *** language ***

    @server.json_post(f"{prefix}/language")
    def _post_language(_req: QSRH, rargs: ReqArgs) -> LangResponse:
        args = rargs["post"]
        input_str = verify_input(args["input"])
        user = verify_token(args["token"])
        return extract_language(db, input_str, user)

    return server, prefix


def setup_server(
        deploy: bool,
        addr: str | None,
        port: int | None) -> tuple[QuickServer, str]:
    if addr is None:
        addr = envload_str("HOST", default="127.0.0.1")
    if port is None:
        port = envload_int("PORT", default=8080)
    return setup(addr, port, parallel=True, deploy=deploy)


def start(server: QuickServer, prefix: str) -> None:
    addr, port = server.server_address
    print(
        f"starting API at http://{addr}:{port}{prefix}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("shutting down..")
        server.server_close()
