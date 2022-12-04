# An element that appear more than half the array
# Time: O(n)
def majorityElement(nums):

    count = {}
    res, maxCount = 0, 0

    for n in nums:

        # get the keys' value in n and add 1, default 0
        count[n] = 1 + count.get(n, 0)

        # we see if the count is bigger than max
        if count[n] > maxCount:

            # we get the max n 
            res = n

        # else we keep current result
        res

        # current count compared to prev max count
        maxCount = max(count[n], maxCount)
    
    return res

print(majorityElement([1,1,2,2,2])) # 2
