# We keep track of both the pos and neg values within array if the max and min are 0 we reset the vals to 1
# Time: O(n), Dynamic Programming
def maxProduct(nums):

    # not 0 cause our val can be a neg
    res = max(nums)

    # we want to multiply current val to self
    currMin = 1
    currMax = 1

    for n in nums:

        # to prevent recomputation bug from currMax
        temp = currMax * n

        # getting the max value
        currMax = max(n * currMax, n * currMin, n) # n because if we had [-1, 4] n is just -4
        
        # getting the min value
        currMin = min(temp, n * currMin, n) # Ex: [-1, -3] could be jsut alone [-3]
        
        res = max(res, currMax, currMin)
    
    return res

print(maxProduct([1,2,-3,4,5]))