'''
Problem: Reverse Integer

Given a signed 32-bit integer 'x', return 'x' with its digits reversed. 
If reversing 'x' causes the value to go outside the signed 32-bit integer 
range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed 
or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
'''
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # store sign and absval x
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        reversed = 0 # res var
        
        while x != 0: # process until every digit is popped
            digit = x % 10 # store trailing digit
            x //= 10 # remove trailing digit
            
            # check for overflow before pushing next digit
            
            # positive overflow
            if (reversed > INT_MAX // 10) or \
                (reversed == INT_MAX // 10 and digit > 7):
                    return 0
                
            # negative overflow
            if (reversed > abs(INT_MIN) // 10) or \
                (reversed == abs(INT_MIN) // 10 and digit > 8):
                    return 0
                
            # build reversed number
            reversed = reversed * 10 + digit
            
        # apply sign
        return sign * reversed