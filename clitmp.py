#!/usr/bin/env python
import os
import sys


# TODO update version
__version__ = "0.0.1"


def exit(m: str, code: int = 0) -> None:
    if m is not None:
        print(e)

    sys.exit(code)


def print_help() -> None:
    usage = f"Usage: {sys.argv[0]} <PATH> <ARGS>\n"
    # TODO update help
    help = """
This is how you use it!
    """[1:-1]

    print(usage)
    print(help)


def get_args() -> str:
    args = sys.argv[1:]

    if not args:
        print_help()
        exit(None, 0)

    if any(map(lambda a: a in args, ["-h", "--help"])):
        print_help()
        exit(None, 0)
    elif any(map(lambda a: a in args, ["-V", "--version"])):
        print(f"{sys.argv[0]} {__version__}")
        exit(None, 0)

    return args


# TODO add something useful
def main() -> None:
    args = get_args()
    print(args)


if __name__ == "__main__":
    main()
