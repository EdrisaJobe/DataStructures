# Factorial function using recursion
# This function calculates n! by multiplying n * (n-1)!
# For example, factorial(4) = 4 * 3 * 2 * 1 = 24

# Visualization of factorial(4):
#
# factorial(4)
#   -> 4 * factorial(3)
#        -> 3 * factorial(2) 
#             -> 2 * factorial(1)
#                  -> returns 1
#             -> 2 * 1 = 2
#        -> 3 * 2 = 6
#   -> 4 * 6 = 24

def factorial(num):
    # Base case: if num is 1 or less, return 1
    if num <= 1:
        return 1    
    
    # Recursive case: multiply num by factorial of (num-1)
    return num * factorial(num - 1)
    
# Test with factorial of 10
print(factorial(10))  # Output: 3628800