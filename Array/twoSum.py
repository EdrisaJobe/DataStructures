def twoSum(arr, tar):

    hashmap = {}

    for i, n in enumerate(arr):
        
        diff = tar - n

        if diff in hashmap:

            return [hashmap[diff],i]

        hashmap[n] = i
    
    return "Target not possible"

print(twoSum([1,2,3,4], 4))


