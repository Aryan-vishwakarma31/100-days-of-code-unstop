import sys
from typing import List, Tuple


def find_judge(n: int, gifts: List[Tuple[int, int]]) -> int:
    """Return the judge (node with in_degree == n-1 and out_degree == 0) or -1.

    Assumes 1-based node labels 1..n.
    """
    if n <= 0:
        return -1

    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    for u, v in gifts:
        if 1 <= u <= n and 1 <= v <= n:
            out_degree[u] += 1
            in_degree[v] += 1

    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            return i

    return -1


def solve():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    # Expect either:
    # 1) First line: n m
    #    following m lines or tokens: a b pairs
    # 2) Single token stream: n m a1 b1 a2 b2 ...

    first = data[0].strip().split()
    try:
        if len(first) >= 2:
            n = int(first[0])
            m = int(first[1])

            tokens = []
            if len(first) > 2:
                tokens.extend(first[2:])
            for line in data[1:]:
                tokens.extend(line.strip().split())

            if len(tokens) < 2 * m:
                print(-1)
                return

            gifts = []
            idx = 0
            for _ in range(m):
                try:
                    a = int(tokens[idx])
                    b = int(tokens[idx + 1])
                except (IndexError, ValueError):
                    print(-1)
                    return
                gifts.append((a, b))
                idx += 2

            print(find_judge(n, gifts))
            return
    except ValueError:
        pass

    # Fallback: token stream
    tokens = ' '.join(data).split()
    if len(tokens) < 2:
        print(-1)
        return

    try:
        n = int(tokens[0])
        m = int(tokens[1])
    except ValueError:
        print(-1)
        return

    if len(tokens) < 2 + 2 * m:
        print(-1)
        return

    gifts = []
    idx = 2
    for _ in range(m):
        try:
            a = int(tokens[idx])
            b = int(tokens[idx + 1])
        except (IndexError, ValueError):
            print(-1)
            return
        gifts.append((a, b))
        idx += 2

    print(find_judge(n, gifts))


if __name__ == '__main__':
    solve()
