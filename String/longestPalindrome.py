# Find the longest palindrome that can be made in a string
# Time: O(n)
def longestPalindrome(string):
    
    odd = 0 # store odd num frequency
    res = [] # word frequency
    count = {}

    for w in string:

        if w not in count:

            # we set each value to 1
            count[w] = 1
        else:
            count[w] += 1

    # grabs the keys values and appending based on conditions
    for times in count.values():
        res.append(times)

        # if odd add to odd
        if times % 2 != 0:
            odd += 1

    # calculations if odd or even
    if odd != 0:
        print(sum(res) - odd + 1)
    elif odd == 0:
        print(sum(res) - odd)

    return res
        
print(longestPalindrome("abccccdd")) # Output: 7 - (dccaccd)



