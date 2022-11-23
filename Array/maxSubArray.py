# Find the subarray which has the largest sum
# Time: O(n) Space: O(1) | Sliding Window
def maxSubArray(nums):

    maxSub = nums[0] # default first index
    current = 0 # saved values

    # going through each element within nums
    for n in nums:
        
        # if any sum is negative, we reset to 0
        if current < 0:
            current = 0
        
        # saving our current number
        current += n

        # we get the max of the current, saving it to maxSub
        maxSub = max(current, maxSub)
    
    return maxSub

print(maxSubArray([-1,3,2,5,8])) # output: 18