# we use a set to hold our values
# Time: O(n) Space; O(n), unique chars
def longestSub(s):

    chars = set()

    # pointer 
    left = 0
    res = 0

    # right pointer goes to all chars
    for right in range(len(s)):

        # when we see a dupe in the set we remove it from left pointer
        while s[right] in chars:

            # remove left char from set and incrment pointer
            chars.remove(s[left])
            left += 1
        
        # once all dupes are gone, we add the char from right pointer
        chars.add(s[right])

        # if window size is > than current window size (r - l + 1)
        res = max(res, right - left + 1)
    
    return res

print(longestSub("abcbba")) # Ouput: 3