def anagram(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    sortedStr1 = {5}
    sortedStr2 = {5}
    print(id(sortedStr1))
    print(id(sortedStr2))

    if id(sortedStr1) == id(sortedStr2):
        return True
    return False

print(anagram('restful', 'fluster'))