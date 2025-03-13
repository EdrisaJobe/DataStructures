# Palindrome Solution Explanation:
# 1. First, we clean the string by:
#    - Converting to lowercase
#    - Removing non-alphanumeric characters
#    - Joining characters into a new string
# 2. Then we use two pointers (left and right) to compare characters from both ends
# 3. If characters don't match, it's not a palindrome
# 4. If we make it through all comparisons, it is a palindrome

def palindrome(s):
    # Clean the string - keep only alphanumeric chars in lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())

    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(palindrome("A man, a plan, a canal: Panama"))