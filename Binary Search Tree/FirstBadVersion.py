# API which returns wether version is bad, implement to find first bad version
# Time: O(log N) Space: O(1) - only uses constants for vars
def firstBadVer(nums):

    # from [1 ... nums] to len of nums
    left = 1
    right = nums

    while left <= right:

        # left +, to prevent overflow in the case the array becomes HUGE and no longer becomes int limit (inf loop)
        mid = left + (right - left) // 2
        
        # seeing if mid in API
        if isBadVersion(mid):

            # we set the right pointer to now be the new boundary
            right = mid
        else:

            # else if we don't see the val in the API we move left pointer
            left = mid + 1

    return left

print(firstBadVer([1,2,3,4,5,6]))# left = 1, right = 6, mid = 3, badVersion = 3    

