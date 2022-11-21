# 
# O(n) Time, O(1) Space
def ProductExceptSelf(nums):

    result = [1] * len(nums) # [1,1,1,1]

    prefix = 1 # [1] [1,2,3,4]
    postfix = 1 # [1,2,3,4] [1]

    
    for i in range(len(nums)):

        # we take save the elements amd put them in the prefix
        # we then take those elements and multiply them by the input
        result[i] = prefix
        prefix *= nums[i]

    # we do -1, -1, -1 since we're working backwards from the last digit to the beginning
    for i in range(len(nums) -1, -1, -1):

        # same result as the prefix but doing the inverse to get the backwards output
        result[i] *= postfix
        postfix *= nums[i]
    
    return result

print(ProductExceptSelf([1,2,3,4]))
# input 4*3*2=24, 3*4=12, 2*4=8, 2*3=6 (exclude element 1)