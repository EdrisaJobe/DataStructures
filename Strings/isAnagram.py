
# word that can be spelt the same ex: care = race, can be spelt either way
def isAnagram(str1,str2):

    # we see if the length are same
    if len(str1) != len(str2):

        return False
    
    # we sort both strings to check ordering
    str1 = sorted(str1)
    str2 = sorted(str2)

    # loop and check each index seeing if elements match
    for i in range(len(str1)):

        if str1[i] == str2[i]:

            return True
        
        return False

print(isAnagram("word", "ordw")) # True
    
    

