class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, value):
        '''Insert new node at beginning.'''
        new_node = ListNode(value, self.head)
        self.head = new_node
        
    def delete(self, value):
        '''delete first occurrence of a node with given value.'''
        if not self.head:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        prev, curr = self.head, self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return
            prev, curr = curr, curr.next