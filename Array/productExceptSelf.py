# 
# O(n) Time, O(1) Space
def ProductExceptSelf(nums):

    result = [1] * len(nums) # [1,1,1,1]

    prefix = 1 # [1,2,6,24]
    postfix = 1 # [24,24,12,4]


    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums) -1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result

print(ProductExceptSelf([1,2,3,4]))
# input 4*3*2=24, 3*4=12, 2*4=8, 2*3=6 (exclude element 1)