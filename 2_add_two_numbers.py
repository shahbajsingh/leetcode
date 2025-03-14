'''
Problem: Add Two Numbers

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() # dummy node to track head
        curr = dummy # curr node pointer
        carry = 0 # carry value to track sum
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val # add l1 to carry
                l1 = l1.next
            if l2:
                carry += l2.val # add l2 to carry
                l2 = l2.next 
            curr.next = ListNode(carry % 10) # add carry to curr node
            carry //= 10 # update carry
            curr = curr.next 
            
        return dummy.next # return head node
        