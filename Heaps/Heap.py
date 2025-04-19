# Python's heap is a Min Heap Implementation
# A min heap is a complete binary tree where the value of each node is less than or equal to the values of its children
# Only the last level can be not fully filled
class Heap:
    def __init__(self):
        # Initialize with [0] to simplify index calculations
        # This way, for any element at index i:
        # - Left child is at 2*i
        # - Right child is at 2*i + 1
        # - Parent is at i//2
        self.heap = [0]

    def push(self, val):
        # Add the new value to the end of the heap
        self.heap.append(val)
        # Get the index of the newly added element
        i = len(self.heap) - 1

        # Heapify up (bubble up or percolate up) operation
        # While the current element is smaller than its parent, swap them
        # This maintains the min-heap property where parent is smaller than children
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            # Swap the current element with its parent
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            # Move up to the parent position
            i = i // 2

    def pop(self):
        # If heap is empty (only contains the placeholder 0)
        if len(self.heap) == 1:
            return None
        # If heap has only one element
        if len(self.heap) == 2:
            return self.heap.pop()

        # Store the minimum value (root) to return later
        res = self.heap[1]   
        # Move last value to root position
        self.heap[1] = self.heap.pop()
        i = 1
        
        # Heapify down (percolate down) operation
        # Continue until we reach a leaf node or the heap property is restored
        while 2 * i < len(self.heap):
            # Check if right child exists, is smaller than left child,
            # and is smaller than current element
            if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                # Swap with right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            # Check if left child is smaller than current element
            elif self.heap[i] > self.heap[2 * i]:
                # Swap with left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                # Heap property is satisfied, exit loop
                break
        return res

    def heapify(self, arr):
        
        # Add the first element to the end to maintain 1-indexed heap
        # (element at index 0 is a placeholder)
        arr.append(arr[0])

        self.heap = arr
        # Start from the last non-leaf node (parent of the last element)
        curr = (len(self.heap) - 1) // 2

        # Process all nodes from the last non-leaf node up to the root
        while curr > 0:
            # Store the current node index
            i = curr 
            # Heapify down (percolate down) operation
            # Continue until we reach a leaf node or the heap property is restored
            while 2 * i < len(self.heap):
                # Check if right child exists, is smaller than left child,
                # and is smaller than current element
                if (2 * i + 1 < len(self.heap) and 
                    self.heap[2 * i + 1] < self.heap[2 * i] and 
                    self.heap[i] > self.heap[2 * i + 1]):
                    # Swap with right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    # Move down to the right child position
                    i = 2 * i + 1
                # Check if left child is smaller than current element
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap with left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    # Move down to the left child position
                    i = 2 * i
                else:
                    # Heap property is satisfied (current node is smaller than both children)
                    # Exit the inner loop and move to the next parent node
                    break
            # Move to the previous parent node
            curr -= 1

'''
Min Heap Visualization:

Example operations:
1. Create empty heap: [0]
2. Push 5: [0, 5]
3. Push 3: [0, 3, 5]
   - 3 is pushed at index 2
   - 3 < 5, so swap: [0, 3, 5]
4. Push 8: [0, 3, 5, 8]
5. Push 1: [0, 1, 3, 8, 5]
   - 1 is pushed at index 4
   - 1 < 3, so swap: [0, 1, 3, 8, 5]

Visual representation:
    1
   / \
  3   5
 /
8

Pop operation:
1. Pop from [0, 1, 3, 8, 5]
   - Return 1 (root)
   - Move 5 to root: [0, 5, 3, 8]
   - Heapify down:
     - 5 > 3, swap with left child: [0, 3, 5, 8]

Final heap after pop:
    3
   / \
  8   5
'''