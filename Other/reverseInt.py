# reverse the integer numbers, time is O(log n) where n is # of digits in the integer space is O(1)
def reverseInt(n):
    
    # remainder
    rem = 0
    # reversed int
    rev = 0
    
    # loop when n is bigger than 0 
    while n > 0:
        # getting the remainder of the n value 1234 % 10 = 4 -> 123 % 3 = 3 -> 12 % 10 = 2 -> 1 % 10 = 0
         rem = n % 10
         # dividing the int by 10 to get 1234 / 10 = 123 -> 123 / 10 = 12 -> 12 /10 = 1 -> 1 / 10 = 0
         # double // is int division
         n = n // 10
         # calculating the reversed multiplied by 10 and adding the remainder in each iteration, rev is 4 -> 43 -> 432 -> 4321
         rev = rev * 10 + rem
    return rev
if __name__ == '__main__':
    print(reverseInt(1234))