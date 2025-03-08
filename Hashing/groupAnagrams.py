
# This code groups anagrams together from a list of strings
# An anagram is a word formed by rearranging letters of another word (e.g. "eat" and "ate")

from collections import defaultdict

# Time Complexity: O(n * k * log k) where:
# n is the number of strings in input list
# k is the maximum length of any string
# The sorting of each string takes O(k log k)

# Space Complexity: O(n * k) where:
# n is the number of strings
# k is the maximum length of any string
# We store all strings in the dictionary

def groupAnagrams(strs):
    # Create a dictionary that will automatically initialize an empty list as value for new keys
    word_dict = defaultdict(list)
    
    # Iterate through each word in the input list
    for w in strs:
        # Sort the characters of the word and join them back together
        # This creates a key that will be the same for all anagrams
        # e.g. both "eat" and "ate" become "aet" when sorted
        word = ''.join(sorted(w))
        
        # Add the original word to the list associated with its sorted version
        word_dict[word].append(w)

    # Return all the grouped anagrams as a list of lists
    return list(word_dict.values())
            
# Example usage:
# Input: ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
