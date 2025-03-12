def quickSort(arr, start, end):
    # Base case: if the subarray has 0 or 1 elements, it's already sorted
    if end - start + 1 <= 1:
        return arr
    
    # Choose the last element as the pivot
    pivot = arr[end]
    # 'left' keeps track of the position where elements smaller than pivot will be placed
    left = start

    # Iterate through the subarray (excluding the pivot)
    for i in range(start, end):
        # If current element is less than pivot
        if arr[i] < pivot:
            # Swap the current element with the element at 'left' position
            # This moves smaller elements to the left side
            arr[left], arr[i] = arr[i], arr[left]
            # Increment 'left' to mark the next position for a smaller element
            left += 1
    
    # Place the pivot in its correct sorted position by swapping with the element at 'left'
    arr[end], arr[left] = arr[left], pivot

    # Recursively sort the left subarray (elements smaller than pivot)
    quickSort(arr, start, left - 1)
    # Recursively sort the right subarray (elements greater than pivot)
    quickSort(arr, left + 1, end)

    # Return the sorted array
    return arr

# Time Complexity:
# - Best case: O(n log n) when the pivot divides the array evenly
# - Average case: O(n log n) - most people choose this
# - Worst case: O(n²) when the array is already sorted or reverse sorted
#   (this implementation always picks the last element as pivot)

# Space Complexity:
# - O(log n) for the recursion stack in the average case
# - O(n) in the worst case when the recursion depth reaches n levels

# For the initial call:
# start should be 0 (beginning of array)
# end should be len(arr) - 1 (last index of array)
arr = [4, 2, 1, 6, 7, 3]
print(quickSort(arr, 0, len(arr) - 1))
