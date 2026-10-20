def calculate_pairs(n, arr):
    from collections import defaultdict
    import bisect

    # Map to store intervals [L, R] for each sum
    sum_intervals = defaultdict(list)

    # Step 1: Find sum for every subarray and store [L, R]
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            sum_intervals[current_sum].append((i, j))

    total_pairs = 0

    # Step 2: For each sum, count pairs of non-overlapping intervals
    for intervals in sum_intervals.values():
        num_intervals = len(intervals)
        if num_intervals < 2:
            continue

        # Extract left endpoints for efficient searching
        left_bounds = [interval[0] for interval in intervals]

        for i in range(num_intervals):
            _, r1 = intervals[i]
            # Find first interval whose start index L2 > R1
            idx = bisect.bisect_right(left_bounds, r1, lo=i + 1)
            total_pairs += num_intervals - idx

    return total_pairs


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()
    if not data:
        return

    n = int(data[0])
    arr = list(map(int, data[1 : n + 1]))

    result = calculate_pairs(n, arr)
    print(result)


if __name__ == "__main__":
    main()
