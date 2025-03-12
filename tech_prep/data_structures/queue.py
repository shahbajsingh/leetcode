from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, item):
        '''Add item to end of queue.'''
        self.queue.append(item)
        
    def dequeue(self):
        '''Remove and return front item of queue.'''
        if self.is_empty():
            return None
        return self.queue.popleft()
    
    def peek(self):
        '''Return front item without removing it.'''
        return self.queue[0] if not self.is_empty() else None
    
    def is_empty(self):
        '''Check if queue is empty.'''
        return len(self.queue) == 0