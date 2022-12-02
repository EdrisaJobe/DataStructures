# reverse an array [1, 2, 3, 4, 5] is now [5, 4, 3, 2, 1]

# func that takes in a param of nums and two pointers
def reverseArr(nums):
    
    # grab the first element within the list
    startIndex = 0
    # grab the last element within the list
    endIndex = len(nums) - 1
    
    # loop through the list when the first index is less than the endIndex (backwards swap)
    while endIndex > startIndex:
        
        # start swapping the items
        nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]

        # go forwards drom first index
        startIndex = startIndex + 1
        # go backwards from last index 
        endIndex = endIndex - 1
    
if __name__ == '__main__':
    # make an array of numbers and set it to the reverse
    arr = [1, 2, 3, 4, 5]
    reverseArr(arr)
    print(arr)
        