# API which returns wether version is bad, implement to find first bad version
# Time: O(log N)
def firstBadVer(nums):

    res = 0
    left = 1

    # not a list we can't use lne(n)-1
    right = n

    while left <= right:

        mid = (left + right) // 2
        
        # seeing if mid in API
        if isBadVersion(mid):

            # update res to now be the mid, and move the pointer back
            res = mid
            right = mid - 1
        else:

            # else if we don't see the val in the API we move left pointer
            left = mid + 1

    return res

print(firstBadVer([1,2,3,4,5,6]))# left = 1, right = 6, mid = 3, badVersion = 3    

