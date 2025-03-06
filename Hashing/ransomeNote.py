# Import Counter class from collections module
from collections import Counter

def canConstruct(ransomeNote, magazine):
    """
    Determines if ransomNote can be constructed from magazine letters
    
    Time Complexity: O(n) where n is the length of ransomNote + magazine
    - Creating Counter objects takes O(n) time
    - Iterating through ransomNote characters takes O(k) time where k <= n
    
    Space Complexity: O(1) since Counter objects store at most 26 lowercase letters
    - Counter objects use fixed space regardless of input size
    - Only lowercase English letters are used
    
    Example visualization:
    ransomNote = "aab"
    magazine = "aabbc"
    
    Counter(ransomNote) -> {'a': 2, 'b': 1}
    Counter(magazine) -> {'a': 2, 'b': 2, 'c': 1}
    
    Check each character count in ransomNote:
    'a': 2 <= 2 in magazine ✓
    'b': 1 <= 2 in magazine ✓
    
    All characters have sufficient counts, return True
    """
    # Create Counter object for ransomNote string
    r = Counter(ransomeNote)
    # Create Counter object for magazine string 
    m = Counter(magazine)

    # Iterate through each character and its count in ransomNote
    for c, n in r.items():
        # If character not in magazine or count in magazine is less than needed
        if c not in m or m[c] < n:
            # Return False as we cannot construct the note
            return False
    # Return True if we've checked all characters successfully
    return True

# Test the function with example input
print(canConstruct("a","ab"))