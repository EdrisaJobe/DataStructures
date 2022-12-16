# API which returns wether version is bad, implement to find first bad version
# Time: O(log N)
def firstBadVer(nums):

    res = n
    left = 0

    # not a list we can't use lne(n)-1
    right = n

    while left <= right:

        # left +, to prevent overflow in the case the array becomes HUGE and no longer becomes int limit
        mid = left + (right - left) // 2
        
        # seeing if mid in API
        if isBadVersion(mid):

            # update res to now be the mid, and move the pointer back
            res = mid
            right = mid - 1
        else:

            # else if we don't see the val in the API we move left pointer
            left = mid + 1

    return -1

print(firstBadVer([1,2,3,4,5,6]))# left = 1, right = 6, mid = 3, badVersion = 3    

