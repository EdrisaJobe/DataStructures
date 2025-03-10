# Insertion Sort Algorithm Explanation:
# This algorithm sorts an array by building a sorted portion one element at a time
# It works similar to sorting cards in a hand - you pick a card and insert it in the right position

def insertionSort(nums):
    # Start from second element (index 1) since single element is already sorted
    for right in range(1, len(nums)):
        # Compare current element with the portion on the left
        left = right - 1
        
        # Keep swapping while left element is greater than current element
        while left >= 0 and nums[left + 1] < nums[left]:
            # Swap elements using temporary variable
            temp = nums[left + 1]
            nums[left + 1] = nums[left] 
            nums[left] = temp
            left -= 1
    return nums

# Example visualization for [5,3,1,4,7,6,2]:
# Initial:  [5,3,1,4,7,6,2]
# Pass 1:   [3,5,1,4,7,6,2]  # 3 moves left of 5
# Pass 2:   [1,3,5,4,7,6,2]  # 1 moves to start
# Pass 3:   [1,3,4,5,7,6,2]  # 4 moves before 5
# Pass 4:   [1,3,4,5,7,6,2]  # 7 stays in place
# Pass 5:   [1,3,4,5,6,7,2]  # 6 moves before 7 
# Pass 6:   [1,2,3,4,5,6,7]  # 2 moves to correct position
# Final:    [1,2,3,4,5,6,7]

print(insertionSort([5,3,1,4,7,6,2]))