def monotonicDecrease(nums):
    """
    Finds the indices where the array is monotonically decreasing.
    Returns a list of (value, index) pairs that form a monotonically decreasing sequence.
    """
    stack = []

    for i, n in enumerate(nums):
        # Remove elements that are smaller than or equal to current element
        # This ensures the stack maintains strictly decreasing order
        while stack and stack[-1][0] <= n:
            stack.pop()
        
        # Add current element to the stack
        stack.append((n, i))
    
    return stack

# Example of monotonically decreasing function
nums = [4, 2, 3, 1, 5, 7, 6, 8]
result = monotonicDecrease(nums)
print(f"Original array: {nums}")
print(f"Monotonically decreasing sequence: {result}")
# Output will be [(8, 7)]