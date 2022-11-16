# Roman numerals that convert to Ints
# Time: O(n), Space: O(1)

hm = {"I":1,
      "V":5,
      "X":10,
      "L":50,
      "D":500,
      "M":1000}

def romanToInt(s): # s = string

    # sum value
    res = 0

    # for loop until last numeral
    for i in range(len(s)-1):

        if hm[s[i]] < hm[s[i+1]]:
            res = res - hm[s[i]]
        else:
            res = res + hm[s[i]]
    
    # return the values by addition
    return res + hm[s[-1]]

print(romanToInt("M"))
