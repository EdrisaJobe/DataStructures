# 1 - We take in an array and then slap a "window" at some subset
# 2 - Then we record the value at that given subset
# 3 - We grow and then we shrink based on our conditions until we reach the end
# EX: [3,2,-4,6,7] Compare: 3+2=5, negate negs, 5+6=11, 11+7=18, max = 18

def dynamicWindow(nums, target):

    minWindowSize = nums[0]
    currentSum = 0
    windowStart = 0
    windowEnd = 0

    for i in range(len(nums)):
        currentSum += nums[windowEnd]

        while currentSum >= target:

            minWindowSize = min(currentSum, windowEnd - windowStart + 1)
            currentSum -= nums[windowStart]
            windowStart += 1
    
            return minWindowSize

print(dynamicWindow([4,2,2,7,8,1,2,8,10], 8))