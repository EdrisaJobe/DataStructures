def closeDuplicates(nums, k):
    # nums: list of numbers to check
    # k: maximum distance between duplicates we're looking for

    window = set()  # Create an empty set to track elements in our current window
    left = 0  # Initialize the left pointer of our sliding window

    for right in range(len(nums)):  # Iterate through the array with right pointer
        
        # If our window size exceeds k, remove the leftmost element and move left pointer
        if right - left + 1 > k:
            window.remove(nums[left])
            left += 1 
            
        # Check if the current element already exists in our window
        if nums[right] in window:
            return True  # If duplicate found within window of size k, return True
            
        window.add(nums[right])  # Add the current element to our window set
    
    return False

print(closeDuplicates([1,2,3,2,6], 4)) # True because there's a dupe from 2 to the other 2 with a size of 3 total, 4 declares distance