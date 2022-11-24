# Find the subarray which has the largest sum
# Time: O(n) Space: O(1) | Sliding Window
def maxSubArray(nums):

    maxSub = nums[0] # default first index
    current = 0 # saved values

    # going through each element within nums
    for n in nums:
        
        # if any sum value is negative, we reset to 0
        if current < 0:
            current = 0
        
        # adding the elements if positive
        current += n

        # we get the max of the current, saving it to maxSub
        maxSub = max(maxSub, current)
    
    return maxSub

print(maxSubArray([-1,3,2,5,8])) # output: 18
                  # [0, 3+2=5, 5+5=10, 10+8=18]