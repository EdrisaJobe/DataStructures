# Time = O(log n) Space = O(1)
def binarySearch(arr, target):
    # First, sort the array since binary search requires a sorted array
    arr = sorted(arr)
    # Initialize pointers to the start and end of the array
    left, right = 0, len(arr)-1

    # Continue searching as long as the search space is valid
    while left <= right:
        # Calculate the middle index
        mid = (right + left) // 2

        # If target is greater than the middle element, search the right half
        if target > arr[mid]:
            left = mid + 1
        # If target is less than the middle element, search the left half
        elif target < arr[mid]:
            right = mid - 1
        # If target equals the middle element, we found it!
        else:
            return mid

    # If we exit the loop without finding the target, it's not in the array
    return -1
        
print(binarySearch([8,4,5,7,3,2,1,6], 3))
"""
Binary Search Visualization:

Original array: [8,4,5,7,3,2,1,6]
After sorting: [1,2,3,4,5,6,7,8]

Iteration 1:
left=0, right=7, mid=3
arr[mid]=4, target=3
Since 3 < 4, search left half
right = mid-1 = 2

Iteration 2:
left=0, right=2, mid=1
arr[mid]=2, target=3
Since 3 > 2, search right half
left = mid+1 = 2

Iteration 3:
left=2, right=2, mid=2
arr[mid]=3, target=3
Since 3 == 3, return mid (2)

Result: Target 3 found at index 2 in the sorted array
"""