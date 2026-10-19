import sys
from typing import List


def kth_distinct(strings: List[str], k: int) -> str:
    """Return the k-th distinct string in `strings` preserving order, or '-1'.

    k is 1-based.
    """
    if k <= 0:
        return '-1'

    unique = list(dict.fromkeys(strings))
    if len(unique) >= k:
        return unique[k - 1]
    return '-1'


def solve():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    # Try two common formats:
    # Format A:
    #   First line: n k
    #   Second line: s1 s2 ... sn
    # Format B:
    #   Tokens: n s1 s2 ... sn k

    # Try Format A first
    first = data[0].strip().split()
    try:
        if len(first) >= 2:
            # could be n k
            n = int(first[0])
            k = int(first[1])
            # gather strings from the rest of the input (remaining lines joined)
            rest_tokens = []
            if len(first) > 2:
                # case: first line had extra tokens after n and k
                rest_tokens.extend(first[2:])
            for line in data[1:]:
                rest_tokens.extend(line.strip().split())

            strings = rest_tokens[:n]
            if len(strings) < n:
                print(-1)
                return

            print(kth_distinct(strings, k))
            return
    except ValueError:
        # not format A — fall through to Format B
        pass

    # Format B: tokens
    tokens = ' '.join(data).split()
    if len(tokens) < 2:
        print(-1)
        return

    try:
        n = int(tokens[0])
    except ValueError:
        print(-1)
        return

    if len(tokens) < 2 + n:
        print(-1)
        return

    strings = tokens[1:1 + n]
    try:
        k = int(tokens[1 + n])
    except (IndexError, ValueError):
        print(-1)
        return

    print(kth_distinct(strings, k))


if __name__ == '__main__':
    solve()
