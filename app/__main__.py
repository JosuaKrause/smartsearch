import argparse

from app.api.server import setup_server, start
from app.misc.util import python_module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=f"python -m {python_module()}",
        description="Run the API server")
    parser.add_argument(
        "--address",
        default=None,
        help="the address of the API server")
    parser.add_argument(
        "--port",
        default=None,
        type=int,
        help="the port of the API server")
    parser.add_argument(
        "--dedicated",
        default=False,
        action="store_true",
        help="whether the server runs in a deployment")
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    server, prefix = setup_server(
        deploy=args.dedicated,
        addr=args.address,
        port=args.port)
    start(server, prefix)


if __name__ == "__main__":
    run()
