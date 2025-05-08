def monotonic(nums):

    res = [0] * len(nums)
    stack = []

    for i, n in enumerate(nums):

        while stack and stack[-1][0] < n:

            stack_N, stack_I = stack.pop()
            res[stack_I] = (i - stack_I)
        
            stack.append((i, n))
    return stack

print(monotonic([2,3,4,1,10,7]))