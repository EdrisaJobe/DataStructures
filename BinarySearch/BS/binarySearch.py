# Binary search function that takes a sorted array and target value as input
def binarySearch(nums, target):

    # Initialize left and right pointers to start and end of array
    left, right = 0, len(nums)-1

    # Continue searching while left pointer is less than or equal to right
    while left <= right:

        # Calculate middle index
        mid = (left + right) // 2

        # If target is greater than rightmost value, search right half
        if target > nums[right]:

            # Move left pointer to right of middle
            left = mid + 1

        # If target is less than leftmost value, search left half
        if target < nums[left]:

            # Move right pointer to left of middle
            right = mid - 1
        
        # Target must be at middle index
        else:

            # Return the middle index where target was found
            return mid
        
    # Target not found in array, return -1
    return -1

# Test the binary search function with sample input
print(binarySearch([1,2,3,4,5,6,7,8,9]))