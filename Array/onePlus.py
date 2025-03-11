def onePlus(digits):
    # Function takes an array of digits representing a number and adds 1 to it
    
    for i in range(len(digits)-1, -1, -1):
        # Loop through digits from right to left
        
        if digits[i] < 9:
            # If current digit is less than 9, we can simply add 1
            
            digits[i] += 1  # Add 1 to current digit
            return digits   # Return the result since no carry over needed
        else:
            digits[i] = 0  # Current digit is 9, set it to 0 and continue loop for carry
    
    return [1] + digits  # If we get here, all digits were 9, so add 1 at start
    
# Example visualization:
# Input: [1,2,9]
# First iteration (i=2): digits[2]=9, so set to 0
# Second iteration (i=1): digits[1]=2, add 1 and return
# Result: [1,3,0]

# Input: [9,9,9]
# All iterations set digits to 0
# Final step adds 1 at start
# Result: [1,0,0,0]

# Time = O(n) | Space = O(n)