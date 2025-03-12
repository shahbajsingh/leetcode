class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        '''Add item to top of stack.'''
        self.stack.append(item)
        
    def pop(self):
        '''Remove and return top item of stack.'''
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        '''Return top item without removing it.'''
        return self.stack[-1] if not self.is_empty() else None
    
    def is_empty(self):
        '''Check if stack is empty.'''
        return len(self.stack) == 0