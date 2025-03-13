# Most Common Word Problem
# Time Complexity: O(n) where n is length of paragraph string
# Space Complexity: O(m) where m is number of unique words

# This function finds the most frequent word in a paragraph that isn't in the banned list
# For example: commonWord("this is this! a test, and test", "test") returns "this"

# Visualization of the process:
# Input: "this is this! a test, and test", banned="test"
#
# After normalization: "this is this a test and test"
#
# Word counting:
# this: 2
# is: 1
# a: 1
# test: 2 (ignored since banned)
# and: 1
#
# Result: "this" (frequency = 2)

def commonWord(paragraph, banned):
    # Dictionary to store word counts
    count = {}
    # Convert banned words to set
    banned = set(banned.split())

    # Normalize string - convert to lowercase and replace punctuation with spaces
    normal_str = ''.join(char.lower() if char.isalnum() else ' ' for char in paragraph).split()

    # Count frequency of each non-banned word
    for word in normal_str:
        if word not in banned:
            count[word] = count.get(word, 0) + 1

    # Find word with highest frequency
    curr_max = 0
    max_word = ''
    for word in count:
        if count[word] > curr_max:
            curr_max = count[word]
            max_word = word
    
    return max_word

print(commonWord("this is this! a test, and test", "test"))