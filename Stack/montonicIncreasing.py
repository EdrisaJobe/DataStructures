def monotonicIncrease(nums):
    """
    Finds the indices where the array is monotonically increasing.
    Returns a list of (value, index) pairs that form a monotonically increasing sequence.
    """
    stack = []

    for i, n in enumerate(nums):
        # Remove elements that are greater than or equal to current element
        # This ensures the stack maintains strictly increasing order
        while stack and stack[-1][0] >= n:
            stack.pop()
        
        # Add current element to the stack
        stack.append((n, i))
    
    return stack

# Example of monotonically increasing function
nums = [4, 2, 3, 1, 5, 7, 6, 8]
result = monotonicIncrease(nums)
print(f"Original array: {nums}")
print(f"Monotonically increasing sequence: {result}")
# Output will be [(1, 3), (5, 4), (6, 6), (8, 7)]