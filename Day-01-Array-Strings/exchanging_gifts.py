import sys

def find_youngest_member(n, m, gifts):
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    for u, v in gifts:
        out_degree[u] += 1
        in_degree[v] += 1

    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            return i

    return -1

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    gifts = []
    index = 2
    for _ in range(m):
        a_i = int(input_data[index])
        b_i = int(input_data[index + 1])
        gifts.append((a_i, b_i))
        index += 2

    result = find_youngest_member(n, m, gifts)
    print(result)

if __name__ == "__main__":
    main()
