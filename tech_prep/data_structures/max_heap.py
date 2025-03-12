import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, value):
        '''Insert value into max heap (invert for max behavior).'''
        heapq.heappush(self.heap, -value)
        
    def pop(self):
        '''Remove and return max value.'''
        return -heapq.heappop(self.heap)
    
    def peek(self):
        '''Return max value without removing it.'''
        return -self.heap[0] if self.heap else None
