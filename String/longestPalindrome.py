# Algorithm explanation:
# 1. We use a set to track characters we've seen an odd number of times
# 2. For each character in the string:
#    - If we've seen it before (it's in the set), we remove it (now we have an even count)
#      and add 2 to our length (we can use this pair in our palindrome)
#    - If we haven't seen it, we add it to the set
# 3. If there are any characters left in the set, we can use one of them as the center
#    of the palindrome, so we add 1 to the length
# 4. Return the final length
def longestPalindrome(s):
    count = set()
    length = 0

    for c in s:
        if c in count:
            count.remove(c)  # Found a pair
            length += 2      # Add this pair to our palindrome
        else:
            count.add(c)     # First occurrence of this character

    # We can use one character with odd frequency as the center of the palindrome
    if count:
        length += 1

    return length
print(longestPalindrome("abbbbc"))# 5 because bbabb or bbcbb
# Visualization example:
# For string "aabcc":
# 1. 'a' -> add to set: {'a'}, length = 0
# 2. 'a' -> remove from set: {}, length = 2
# 3. 'b' -> add to set: {'b'}, length = 2
# 4. 'c' -> add to set: {'b', 'c'}, length = 2
# 5. 'c' -> remove from set: {'b'}, length = 4
# 6. Set is not empty, so length += 1
# 7. Return length = 5 (can form "abcba" or "acbca")