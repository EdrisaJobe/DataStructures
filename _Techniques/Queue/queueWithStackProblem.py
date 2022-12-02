# Queue with stack
# FIFO, LIFO problem - we pop the last item from enqueue then insert it into the dequeue
class Qws:

    def __init__(self):

        self.enqueueStack = []
        self.dequeueStack = []

        # O(1) - runtime
    def enqueue(self, data):
        return self.enqueueStack.append(data)

        # O(n) - runtime
    def dequeue(self):

        # if both stacks are empty, raise an Exception error
        if len(self.enqueueStack) == 0 and len(self.dequeueStack) == 0:
            raise Exception('Empty stacks...')

        # if the dequeue stack is empty, we have to copy enqueueStack to dequeueStack
        if len(self.dequeueStack) == 0:
            
            # if enqueue is not empty, we add last item to dequeue
            while len(self.enqueueStack) != 0:
                self.dequeueStack.append(self.enqueueStack.pop())

        # O(1) - otherwise just return the last item from dequeue
        return self.dequeueStack.pop()


queueStack = Qws()

queueStack.enqueue(23)
queueStack.enqueue(62)
queueStack.enqueue(44)
queueStack.enqueue(13)

print(queueStack.dequeue())
print(queueStack.dequeue())
print(queueStack.dequeue())