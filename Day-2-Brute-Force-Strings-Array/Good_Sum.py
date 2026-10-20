def good_sum(N, A):
    """
    Write your logic here.
    Parameters:
        N (int): The number of elements in the array
        A (list): The array of integers
    Returns:
        int: The final sum after performing the mentioned operation
    """
    stack = []
    for x in A:
        if x < 0:
            target = abs(x)
            current_sum = 0
            # Remove elements from the stack moving left from x until their sum >= |x|
            while stack and current_sum < target:
                current_sum += stack.pop()
            # Replace x with its absolute value and push it back
            stack.append(target)
        else:
            stack.append(x)
    return sum(stack)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    A = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = good_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()
