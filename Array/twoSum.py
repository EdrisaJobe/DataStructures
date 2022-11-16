# the sum of two indexes equal to the target sum
def twoSum(arr, tar):

    # save the values in a map (no dupes)
    hashmap = {}

    # we get the index and element
    for i, n in enumerate(arr):
        
        # get the complement
        diff = tar - n

        # we see if the complement is in the map
        if diff in hashmap:

            # return the complement, and index
            return [hashmap[diff],i]

        # else we return the index of the element
        hashmap[n] = i
    
    return "Target not possible"

print(twoSum([1,2,3,4], 4))


