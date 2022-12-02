# word that can be spelt the same back and forwards
def isPalindrome(s):

    # original and reversed vars
    originalStr = s
    reversedStr = reverse(s)

    # if both are the same words return True
    if originalStr == reversedStr:
        return True
    return False

def reverse(data):

    # strings are immutable, we save it as list
    data = list(data)

    # setup two pointers to check each char
    startIndex = 0
    endIndex = len(data)-1

    # a loop to see if start is less than end
    while startIndex < endIndex:

        # swap the chars
        data[startIndex], data[endIndex] = data[endIndex], data[startIndex]

        # increment and decrement the pointers
        startIndex = startIndex + 1
        endIndex = endIndex - 1

    # convert the data to string
    return ''.join(data)

print(isPalindrome("madam"))



