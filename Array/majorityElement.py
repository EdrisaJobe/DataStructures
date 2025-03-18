# An element that appear more than half the array
# Time: O(n)
from collections import Counter 
def majorityElement(nums):
    
    count = Counter(nums)  # Create a Counter object that counts occurrences of each element in nums
    
    maxVal = max(count.values())  # Find the maximum frequency among all elements
                                  # In our example, max of [2,3] is 3
        
    for k, v in count.items():  # Iterate through each key-value pair in the Counter
                                # k is the element, v is its frequency
            
        if v == maxVal:  # If the current element's frequency equals the maximum frequency
            return k   

print(majorityElement([1,1,2,2,2])) # 2  
