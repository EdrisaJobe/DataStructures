def binarySearch(left, right):
    
    while left <= right:
        # Find the middle point
        mid = (left + right) // 2
        
        # Check if mid is the correct value
        result = isCorrect(mid)
        
        if result > 0:
            # If mid is too small, search the right half
            left = mid + 1
        elif result < 0:
            # If mid is too large, search the left half
            right = mid - 1
        else:
            # Found the correct value
            return mid
    
    # If we exit the loop without finding the target, it doesn't exist
    return -1


def isCorrect(num):
    """
    Helper function that compares a number with the target value (10).
    Returns:
    - 1 if num > 10 (too large)
    - 2 if num < 10 (too small)
    - 0 if num = 10 (correct)
    """
    if num > 10:
        return 1
    elif num < 10:
        return -1 
    else:
        return 0

print(isCorrect(10))
"""
Binary Search Visualization:

Example: binarySearch(1, 20) to find the value 10

Iteration 1:
left=1, right=20, mid=10
isCorrect(10) = 0
Since result = 0, return mid (10)

Example: binarySearch(1, 20):

Iteration 1:
left=1, right=20, mid=10
isCorrect(10) = 0
Since result = 0, return mid (10)

Iteration 2 (if we didn't return):
left=1, right=9, mid=5
isCorrect(5) = 2
Since result > 0 (but it should be < 0), left = mid + 1 = 6

The bug in isCorrect causes the binary search to move in the wrong direction
when the target is not found immediately.
"""
