# Import Counter class from collections module to count character frequencies
from collections import Counter

# Function that finds length of longest palindrome that can be built from input string
# Time: O(n) where n is length of input string - we iterate through string once to count frequencies
# Space: O(k) where k is number of unique characters in string - we store character counts in Counter
# Example:
# Input: "abccccdd"
# Character counts: {'a':1, 'b':1, 'c':4, 'd':2}
# Can use: 4 'c's (2 pairs), 2 'd's (1 pair), and 1 'a' or 'b' in middle
# Result: "dccaccd" (length 7)
def longestPalindrome(s):
        
    # Count frequency of each character in input string
    count = Counter(s)
    # Track how many pairs of characters we can use
    result = 0

    # For each character count in our frequency counter
    for n in count.values():
        # Add number of complete pairs we can make (n divided by 2 rounded down)
        result += n // 2
        
    # If we have any single characters left over (total pairs * 2 < string length)
    if result * 2 < len(s):
        # We can use one single character in middle, so multiply pairs by 2 and add 1
        result = result * 2 + 1
    else:
        # Otherwise just multiply pairs by 2 for total palindrome length
        result *= 2
        
    return result

# Test the function with example input
print(longestPalindrome("abccccdd"))