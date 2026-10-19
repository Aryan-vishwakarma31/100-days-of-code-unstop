import sys
import re
import argparse

COORD_REGEX = re.compile(r'^[a-hA-H][1-8]$')


def determine_color(s: str) -> str:
    """Return the color ("Black" or "White") of a chessboard square given
    a coordinate like 'a1'..'h8'. Raises ValueError on invalid input.
    """
    s = s.strip()
    if not COORD_REGEX.match(s):
        raise ValueError(f"Invalid square coordinate: {s!r}")

    col_char = s[0].lower()
    row_char = s[1]

    col = ord(col_char) - ord('a')
    row = int(row_char) - 1

    return "Black" if (col + row) % 2 == 0 else "White"


def main():
    parser = argparse.ArgumentParser(description="Determine chessboard square color.")
    parser.add_argument('square', nargs='?', help="Square coordinate like a1")
    args = parser.parse_args()

    token = None
    if args.square:
        token = args.square
    else:
        tokens = sys.stdin.read().split()
        if tokens:
            token = tokens[0]

    if not token:
        # No input provided; exit quietly (matches previous behavior)
        return

    try:
        print(determine_color(token))
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
