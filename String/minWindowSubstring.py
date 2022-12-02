# string takes in letters of alphabet, t takes in letters which contiguously display when printed
# EX: string = "ABCDE" t = "BCE" Output: BCDE
# Time: O(n) added each char once and removed each char once
def minSubstring(string, t):

    if t == "" : return ""

    count, window = {}, {}
    res, resLen = [-1, -1], float('infinity')
    left = 0

    for c in t:

        # if char in map we get the value stored and add to count, 0 is default value
        count[c] = 1 + count.get(c, 0)

    # have has our current saved values
    # need allows us to see if we have the right value amounts in count
    have, need = 0, len(count)
    
    for right in range(len(string)):

        # saving the current right pointer value
        c = string[right]
        # if char within the map we get the current window count and store it
        window[c] = 1 + window.get(c, 0)

        # we don't care about chars not in t, so we update our have by 1
        if c in count and window[c] == count[c]:
            
            have += 1
        
        # updating our result only if have and need are same
        while have == need:

            # calc window size less than infinity - (runs at least once)
            if (right - left + 1) < resLen:

                res = [left, right]
                resLen = (right - left + 1)

            # pop from left of window
            window[string[left]] -= 1

            # if the current left value in map and is smaller than the prev left value we remove prev saved value
            if string[left] in count and window[string[left]] < count[string[left]]:

                have -= 1

            left += 1

    # have the updated save values
    left, right = res
        
    # we return the max len, else empty string for invalid input
    return string[left:right + 1] if resLen != float('infinity') else ""

print(minSubstring("ADOBODEBANC", "ODAC")) # ODEBANC