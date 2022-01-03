# palindrome  program, takes in O(n) time due to while loop and O(1) space since oncly one item is printed out.

# func thats takes in string and two vars
def palindrome(s):
    originalStr = s
    reversedStr = reverse(s)
    
    if originalStr == reversedStr:
        return True
    return False

# make data a list and have the elements swap with one another
def reverse(data):
    data = list(data)
    # poiinters that will be used for comparing each element within the list
    # gets the first element
    startIndex = 0
    # get the last element of the list
    endIndex = len(data) - 1
    
    # loops through the array until each of the pointers meet
    while endIndex > startIndex:
        # swapping the first element with the last element vice-versa
        data[startIndex] = data[endIndex]
        data[endIndex] = data[startIndex]
        
        # increment of the first index to the right forward
        startIndex = startIndex + 1
        # decrement of the last index to the left backwards
        endIndex = endIndex - 1
    # transform and return data as a string
    return ''.join(data)

# call the function
if __name__ == '__main__':
    
    print(palindrome('madam')) # True
    print(palindrome('shoes')) # False
    
    data = [123,3]
    data2 = data
    data2.append(100)
    print(data)