# We count the occurance of a char within a map 
# (EX: ABABBA both pointers at the start, check to see if string <= n)
# Time: O(26 * n) where 26 is num of chars
def longestRepeatingSub(string, n):

    count = {}
    res = 0 
    left = 0

    for right in range(len(string)):

        # we get the key within map and increment it's count if we get same keys
        count[string[right]] = 1 + count.get(string[right], 0)

        # num of replacements, if greater than n we shift left pointer
        while (right - left + 1) - max(count.values()) > n:

            count[string[left]] -= 1
            left +=1


        # getting the size of window
        res = max(res, right - left + 1)
    
    return res

print(longestRepeatingSub("ABABBA", 2)) # Output: 5