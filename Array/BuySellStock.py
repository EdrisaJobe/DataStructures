# An array where we find the max amount of profit we can make when subtracting the least and biggest numbers
# Time: O(n), Space: O(1)
def BuySellStock(prices):

    # two pointers, min and max checkers
    leftMin = 0
    rightMax = 1

    # max_profit made
    total = 0

    # we loop only if the rightMax is less than array list
    while rightMax < len(prices):

         # we save our max when subtracting max and min to a "current" var
        current = prices[rightMax] - prices[leftMin]

        if prices[leftMin] < prices[rightMax]:

           # we take the max between the current val and total val
            total = max(current, total)

        else:

            # we move left pointer to where right pointer is
            leftMin = rightMax

        # incrment the right pointer by 1
        rightMax +=1

    return total

print(BuySellStock([6,7,4,5,2,8])) # max_profit of: 6


