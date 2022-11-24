# 1 - We take in an array and then slap a "window" at some subset
# 2 - Then we record the value at that given subset
# 3 - We then slide the "window" to the next values and record that data
# 4 - We record the max from the subset with the highest value and repeat until the end
# EX: [3,2,-1,5] Compare: 3+2=5, 2-1=1, -1+5=4, max = 5

def maxSubArra(nums, k):

    maxVal = nums[0]
    currentSum = 0

    for i in range(len(nums)):

        currentSum += nums[i]

        if i >= k - 1:

            maxVal = max(currentSum, maxVal)
            currentSum -= nums[i - (k - 1)]
    
    return maxVal

    
print(maxSubArra([3,2,-1,5], 2))


