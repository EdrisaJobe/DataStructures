# We fidn the target within an array, return -1 if no target else return index
# Time: O(log n) - divide & conquer
def search(nums, target):

    # pointers 
    left = 0
    right = len(nums)-1

    while left < right:

        # we get the mide value
        mid = (left + right) // 2

        # if the mid is the target we return our value
        if nums[mid] == target:
            return mid

        # if mid greater than target, decrement right pointer
        elif nums[mid] > target:

            right -= 1
        
        # mid less than target, increment left pointer
        else:
            left += 1

    return -1

print(search([1,2,3], 3))
