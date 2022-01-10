# we want to find the max left and max right values and subtract the smaller number from the height
def trappedRainWater(height):
    
    # base case of 3 in order to get a solution
    if len(height) < 3:
        return 0
    
    # a list which takes in 0 values from a max left and right list
    left_max = [0 for _ in range(len(height))]
    right_max = [0 for _ in range(len(height))]
    
    # left max values calculation, we take in 1 since the left max already has a 0 meaning can't take in water
    # [2,1,0,3,2,3] = MAX([0,2,2,2,3,3,3]) checking backwards
    for i in range(1, len(height)):
        
        # the indexes of the left max is checking to see the max height of the prev value, so -1
        # first item is 0 by default
        left_max[i] = max(left_max[i-1], height[i-1])
    
    # dealing with right max values | [2,1,0,3,2,1] = MAX([3,3,3,3,3,3,0]) checking forwards
    # last value also starts with initial value of 0, so we start with -2
    for i in range(len(height) -2, -1, -1):
        
        # checking the items in front, so +1
        right_max[i] = max(right_max[i+1], height[i+1])
    
    # will display the amount of rain water trapped
    trapped = 0
    
    # no need to deal with the front and last items as they are both 0
    for i in range(1, len(height)-1):
        # if the min of left and right is bigger than the current element
        if min(left_max[i], right_max[i]) > height[i]:
            trapped += min(left_max[i], right_max[i]) - height[i]
    
    return trapped

if __name__ == '__main__':
    print(trappedRainWater([1,0,2,1,3,1,2,0,3]))