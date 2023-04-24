import argparse

from app.misc.util import python_module
from app.system.config import get_config
from app.system.ops.ops import get_ops


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=f"python -m {python_module()}",
        description="Initialize subsystems.")
    parser.add_argument(
        "--init-db",
        default=False,
        action="store_true",
        help="create all tables")
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    ops = get_ops("db", get_config())
    if args.init_db:
        ops.init()


if __name__ == "__main__":
    run()
