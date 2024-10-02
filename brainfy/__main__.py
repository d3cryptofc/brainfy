import argparse
import sys

from brainfy import Interpreter


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            'An amazing interpreter for the esoteric language brainf*ck '
            'written in Python.'
        )
    )
    parser.add_argument(
        'FILE',
        help='read BF script instructions from file',
        type=argparse.FileType('r')
    )
    args = parser.parse_args()

    try:
        Interpreter().run(args.FILE)
    except RuntimeError as e:
        print('ERROR:', str(e), file=sys.stderr)
        exit(1)



