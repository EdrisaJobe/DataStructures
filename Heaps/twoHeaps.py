import heapq

class TwoHeaps:
    """
    A class that uses two heaps to efficiently find the median of a stream of numbers.
    
    Visualization:
    
    self.small (max heap)    |    self.large (min heap)
    [larger elements]        |    [smaller elements]
    stored as negatives      |    stored as positives
    --------------------------+---------------------------
    -3 (stored as 3)         |    4
    -2 (stored as 2)         |    5
    -1 (stored as 1)         |    6
    
    The median is either:
    - The top of small (negated) if small has more elements
    - The top of large if large has more elements
    - The average of both tops if they have equal elements
    """

    def __init__(self):
        """
        Initialize two heaps:
        - small: a max heap (implemented as a min heap with negated values)
        - large: a min heap
        
        These heaps will store numbers in such a way that:
        - small contains the smaller half of the numbers
        - large contains the larger half of the numbers
        """
        self.small = []  # Max heap (implemented using min heap with negative values)
        self.large = []  # Min heap

    def insert(self, num):
        """
        Insert a new number into the data structure and rebalance the heaps.
        
        The method:
        1. Adds the new number to the appropriate heap
        2. Ensures heap property (max of small ≤ min of large)
        3. Rebalances heaps so their sizes differ by at most 1
        
        Args:
            nums: The number to insert
        """
        heapq.push(self.small, -1 * num)
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            value = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.small) > len(self.large) + 1:
            value = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * value)
    
    def getMedian(self) -> float:
        """
        Calculate and return the median of all elements inserted so far.
        
        Returns:
            float: The median value
            
        Logic:
        - If small heap has more elements, its top element is the median
        - If large heap has more elements, its top element is the median
        - If both heaps have equal elements, the median is the average of their tops
        """
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2