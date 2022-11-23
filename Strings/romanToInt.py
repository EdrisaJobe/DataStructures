# Roman numerals that convert to Ints
# Time: O(n), Space: O(1)

hm = {"I":1,
      "V":5,
      "X":10,
      "L":50,
      "C":100,
      "D":500,
      "M":1000}

def romanToInt(s): # s = string input

    # output value
    res = 0

    # for loop until last numeral
    for i in range(len(s)-1):

        # we check to see if the prev value is less than the next value within input
        # EX: IV = 1-5 = 4 and VI = 5+1 = 6)
        if hm[s[i]] < hm[s[i+1]]:
            res = res - hm[s[i]]
        else:
            res = res + hm[s[i]]
    
    # we return the new values within our whole input
    return res + hm[s[-1]]

print(romanToInt("CMXCVIII")) # 998
