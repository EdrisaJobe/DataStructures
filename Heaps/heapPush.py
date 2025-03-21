class Heap:
    # This class implements a min-heap data structure

    def __init__(self):
        # Constructor initializes the heap
        # We start with [0] as the first element to simplify index calculations
        # This way, for any element at index i:
        # - Left child is at 2*i
        # - Right child is at 2*i + 1
        # - Parent is at i//2
        self.heap = [0]

    def push(self, value):
        
        # Add the new value to the end of the heap
        self.heap.append(value)
        # Get the index of the newly added element
        i = len(self.heap) - 1

        # Perform "heapify up" (or "bubble up") operation
        # While the current element is smaller than its parent, swap them
        # This maintains the min-heap property where parent is smaller than children
        while self.heap[i] < self.heap[i // 2]:
            # Store the parent value in a temporary variable
            temp = self.heap[i // 2]
            # Move the current value up to the parent position
            self.heap[i // 2] = self.heap[i]
            # Place the parent value in the current position
            self.heap[i] = temp
            # Update the index to continue checking up the heap
            i = i // 2