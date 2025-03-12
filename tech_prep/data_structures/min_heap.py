import heapq

class MinHeap: # priority queue
    def __init__(self):
        self.heap = []
        
    def push(self, value):
        '''Insert value into heap.'''
        heapq.heappush(self.heap, value)
        
    def pop(self):
        '''Remove and return smallest element.'''
        if self.heap:
            return heapq.heappop(self.heap)
        return None
    
    def peek(self):
        '''Return smallest element without removing it.'''
        return self.heap[0] if self.heap else None