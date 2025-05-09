#!/usr/bin/env python
import sys


# TODO update version
__version__ = "0.0.1"

# INFO version number: (major, minor, micro, releaselevel, and serial)
# INFO release level is one of ['alpha', 'beta', 'candidate', 'final']
assert sys.version_info == (3, 13, 2, "final", 0)
# assert library.__version__ == "1.26.0"


def exit(code: int = 0, msg: str | None = None) -> None:
    if msg is not None:
        print(msg)

    sys.exit(code)


def print_help() -> None:
    usage = f"Usage: {sys.argv[0]} <PATH> <ARGS>\n"
    # TODO update help
    help = "This is how you use it!"

    print(usage)
    print(help)


def error(msg: str) -> None:
    print("\033[1;31m", end="")
    print(f"Error: {msg}")
    print("\033[0m", end="")


def info(msg: str) -> None:
    print("\033[1;32m", end="")
    print(f"Info: {msg}")
    print("\033[0m", end="")


def get_args() -> list[str]:
    args = sys.argv[1:]

    # if len(args) <2:
    if not args:
        print_help()
        exit()

    if any(map(lambda a: a in args, ["-h", "--help"])):
        print_help()
        exit()
    elif any(map(lambda a: a in args, ["-V", "--version"])):
        print(f"{sys.argv[0]} {__version__}")
        exit()

    return args


# TODO add something useful
def main() -> None:
    args = get_args()
    print(args)
    error("Oh no!")
    info("Interesting")


if __name__ == "__main__":
    main()
