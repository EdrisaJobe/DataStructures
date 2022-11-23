#define a function
def factor(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print (factor(5))