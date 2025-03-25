def prefix_sums(arr):
    """
    Calculates the prefix sum array for a given input array.
    
    Time Complexity: O(n) where n is the length of the input array.
    Space Complexity: O(n) for storing the prefix sum array.
    """
    # Get the length of the input array
    n = len(arr)
    
    # Create a prefix sum array with size n+1, initialized with zeros
    # We use n+1 to make calculations easier (prefix[0] = 0)
    prefix = [0] * (n + 1)
    
    # Calculate each prefix sum by adding the current element to the previous sum
    for i in range(1, n + 1):
        # prefix[i] represents the sum of all elements from arr[0] to arr[i-1]
        # prefix[i-1] is the previous prefix sum
        # arr[i-1] is the current element in the original array
        prefix[i] = prefix[i - 1] + arr[i - 1]
    
    # Return the complete prefix sum array
    return prefix

print(prefix_sums([1,2,3,4,5]))

# Visualization of prefix sum calculation
# Example:
# Original array:  [1, 2, 3, 4, 5]
# Prefix sums:     [0, 1, 3, 6, 10, 15]
#                   |  |  |  |  |   |
#                   |  |  |  |  |   └─ Sum of all elements (1+2+3+4+5)
#                   |  |  |  |  └─ Sum of first 4 elements (1+2+3+4)
#                   |  |  |  └─ Sum of first 3 elements (1+2+3)
#                   |  |  └─ Sum of first 2 elements (1+2)
#                   |  └─ Sum of first element (1)
#                   └─ Initial value (0)
