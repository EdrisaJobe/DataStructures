# Fibonacci sequence using recursion
# This function calculates the nth Fibonacci number by adding the previous two numbers
# For example, fibonacci(4) = fibonacci(3) + fibonacci(2) = 3
# The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

# Visualization of fibonacci(4):
#
# fibonacci(4)
#   -> fibonacci(3) + fibonacci(2)
#      fibonacci(3)
#        -> fibonacci(2) + fibonacci(1)
#           fibonacci(2) 
#             -> fibonacci(1) + fibonacci(0)
#                -> returns 1 + 0 = 1
#           fibonacci(1)
#             -> returns 1
#        -> returns 1 + 1 = 2
#      fibonacci(2)
#        -> fibonacci(1) + fibonacci(0)
#        -> returns 1 + 0 = 1
#   -> returns 2 + 1 = 3

def fibunacci(num):
    # Base case: if num is 0 or 1, return num
    if num <= 1:
        return num
    
    # Recursive case: add fibonacci of (n-1) and (n-2)
    return fibunacci(num - 1) + fibunacci(num - 2)

# Test with fibonacci of 10
print(fibunacci(10))  # Output: 55