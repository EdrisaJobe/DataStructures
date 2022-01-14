class Stack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        return self.stack.append(data)
    
    def is_empty(self):
        return self.stack == []
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

s = Stack()

s.push(12)
s.push(54)
s.push(99)

print(s.pop())
print(s.peek())
    