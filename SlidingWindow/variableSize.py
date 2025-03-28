def longestSubarray(nums):
    """
    This function finds the length of the longest subarray containing identical elements.
    
    It uses a variable-size sliding window approach:
    - The 'left' pointer marks the start of the current subarray of identical elements
    - The 'right' pointer expands the window as we iterate through the array
    - When we encounter a different element, we reset the left pointer to the current position
    - We continuously track the maximum length of valid subarrays found
    
    Args:
        nums: A list of elements to check
        
    Returns:
        The length of the longest subarray containing identical elements
    """
    length = 0  # Initialize the maximum length found
    left = 0    # Initialize the left pointer of our sliding window

    for right in range(len(nums)):
        # If current element differs from the element at left pointer,
        # we've found a different element, so reset the left pointer
        if nums[left] != nums[right]:
            left = right 
        
        # Update the maximum length by comparing current length with the new window size
        length = max(length, right - left + 1)
    return length # [1,2,2,3,4,5]


def shortestSubarray(nums, target):
    """
    This function finds the length of the shortest subarray with a sum at least the target.
    
    It uses a variable-size sliding window approach:
    - The 'left' pointer marks the start of the current subarray
    - The 'right' pointer expands the window as we iterate through the array
    - When the sum of the window exceeds the target, we shrink the window from the left
      to find the minimum valid window size
    - We continuously track the minimum length of valid subarrays found
    
    Args:
        nums: A list of numbers to check
        target: The minimum sum we're looking for in the subarray
        
    Returns:
        The length of the shortest subarray with sum at least the target,
        or 0 if no such subarray exists
    """
    left = 0    # Initialize the left pointer of our sliding window
    total = 0   # Initialize the running sum of our window
    length = float("inf")  # Initialize the minimum length found

    for right in range(len(nums)):
        total += nums[right]  # Add the current element to our running sum

        while total >= target:
            length = min(length, right - left + 1)  # Update minimum length
            total -= nums[left]  # Remove leftmost element from sum
            left += 1  # Shrink window from the left
            
    return 0 if length == float("inf") else length

print(shortestSubarray([2,3,1,2,4,3]))