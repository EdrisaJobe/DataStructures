# Binary Search Insert Position
# This algorithm finds the index where a target number should be inserted 
# into a sorted array to maintain the sort order
# Time Complexity: O(log n) where n is length of array
# Space Complexity: O(1)

# Visualization of searchInsert([1,2,4,5], 3):
#
# Initial array: [1, 2, 4, 5], target = 3
# 
# Step 1: left=0, right=3, mid=1
#         [1, 2, 4, 5]
#             ^
#         2 < 3, so search right half
#
# Step 2: left=2, right=3, mid=2  
#         [1, 2, 4, 5]
#                ^
#         4 > 3, so search left half
#
# Step 3: left=2, right=1
#         While loop ends since left > right
#         Return left=2 (correct insert position)

def searchInsert(nums, target):
    # Initialize left and right pointers    
    left, right = 0, len(nums)-1

    # Binary search while left pointer <= right pointer
    while left <= right:
        # Find middle index
        mid = (left + right) // 2

        # If target found at mid, return mid index
        if nums[mid] == target:
            return mid
        # If mid value less than target, search right half
        elif nums[mid] < target:
            left = mid + 1
        # If mid value greater than target, search left half
        else:
            right = mid - 1
        
    # Target not found - return left pointer as insert position
    return left

print(searchInsert([1,2,4,5], 3))
