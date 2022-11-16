# an array that has duplicate numbers must return True or False
# input: [1,1,2,3,4] output: True

def arrayDupe(arr):

    # set is an unordered list {"item1", "item2"...}
    # we compare to see if the set items are not equal to another item
    if len(set(arr)) != len(arr):
        return True
    return False

print(arrayDupe([1,2,2,3,4,5]))
