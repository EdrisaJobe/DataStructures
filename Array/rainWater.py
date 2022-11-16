# maximum amount of water that can be trapped within bars (1 unit)
# Example: [2,1,3,1,4] = height, Output: 3, we can only trap 3 units of water
# Time: O(N) using Dynamic Programming (precompute vals on left and right)
def rainWater(n):

    trapped = 0

    # if n is < 3, we can't trap water (0)
    if len(n) < 3:
        return 0
    
    # left and right max values (height)
    left_max = [0 for _ in range(len(n))]
    right_max = [0 for _ in range(len(n))]

    # iterate from left
    for i in range(1, len(n)):

        # we consider the prev elements then compare with prev bar
        left_max[i] = max(left_max[i - 1], n[i - 1]) # Ex:[0,1,1,2,2,3,3,3]

    # iterate from right (from last digit to 0, we keep decrementing i)
    for i in range(len(n) -2, -1, -1):

        # we consider the prev elements then compare with prev bar
        right_max[i] = max(right_max[i + 1], n[i + 1]) # Ex: [3,3,3,3,3,3,0]

    for i in range(1, len(n)-1):

        # if left min and right min are > height
        if min(left_max[i], right_max[i]) > n[i]:

            # we get the min number from the maxes and subtract from the elements in n
            trapped += min(left_max[i], right_max[i]) - n[i]
        
    return trapped

print(rainWater([2,1,2,1,3]))

        #
# W # W #  = 2
# # # # # 