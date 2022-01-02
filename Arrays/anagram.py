# anagram - restful == fluster ('r', 'e', 's', 't', 'f', 'u', 'l')
# define a func with two params

def anagram(str1, str2):

    # check the len of whether str1 is equal to str2
    if len(str1) != len(str2):
        return False
    
    # sorting each string value as ['a', 'b', 'c']
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    # for loop to iterate adn check the letters with the same indexes
    # len can be str1 or str2 as they both should equal to the same len
    # O(n) runtime
    for i in range(len(str1)):
        
        # checking to see if they match
        if str1[i] != str2[i]:
            return False
    
    # O(N log N) + O(n) = O(N log N) = linearithmic due to the num of letters within each array
    return True

if __name__ == '__main__':
    s1 = ['r', 'e', 's', 't', 'f', 'u', 'l']
    s2 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    print(anagram(s1, s2))
    
    # or
    print(anagram('bro', 'rob'))
        
        