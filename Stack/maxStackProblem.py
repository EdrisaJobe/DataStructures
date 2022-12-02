# we take in a main stack and maximum stack, both 1D arrays
# we compare the main stack with max stack to get the max ints
# the last item will be the max item in the max stack so we print it out
# Runtime: O(1) - pop, Space: O(n) - we store the same amount of ints from main to max stack

class MaxStack:
    
    def __init__(self):
        self.stack = []
        self.maxStack = []
    
    def push(self,data):
        
        self.stack.append(data)

        # if there is an item in the main stack, append to maxStack
        if len(self.stack)==1:
            self.maxStack.append(data)
            return
        
        # when the int is greater than that of last item in the maxStack, we append
        # otherwise we take in the max in the maxStack
        if data>self.maxStack[-1]: # peek operation
            self.maxStack.append(data)
        else:
            self.maxStack.append(self.maxStack[-1])
    
    # we remove the last item in maxStack and then return the last item on the main stack
    def pop(self):
        self.maxStack.pop()
        return self.stack.pop()

    # we get the last item of the maxStack O(1)
    def getMax(self):
        return self.maxStack.pop()

stack = MaxStack()

stack.push(332)
stack.push(112)
stack.push(512)
stack.push(212)

print(stack.getMax())