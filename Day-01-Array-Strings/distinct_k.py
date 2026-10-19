import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    strings = input_data[1:n+1]
    k = int(input_data[n+1])

    unique_strings = list(dict.fromkeys(strings))

    if len(unique_strings) >= k:
        print(unique_strings[k - 1])
    else:
        print(-1)

if __name__ == '__main__':
    solve()
