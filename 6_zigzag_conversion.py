'''
Problem: Zigzag Conversion

The string 'PAYPALISHIRING' is written in a zigzag pattern on 
a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: 'PAHNAPLSIIGYIR'

Write the code that will take a string and make this conversion 
given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = 'PAYPALISHIRING', numRows = 3
Output: 'PAHNAPLSIIGYIR'

Example 2:

Input: s = 'PAYPALISHIRING', numRows = 4
Output: 'PINALSIGYAHRPI'
Explanation:

P    I    N
A  L S  I G
Y A  H R
P    I

Example 3:

Input: s = 'A', numRows = 1
Output: 'A'
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s
        
        rows = [''] * numRows # empty array to hold rows
        
        # flags to track row and traversal direction
        currRow = 0
        travDown = False
        
        
        for char in s: 
            rows[currRow] += char # add curr char to row array at curr index
            
            if currRow == 0 or currRow == numRows - 1:
                travDown = not travDown # flip direction at top/bottom
                
            currRow += 1 if travDown else -1 # move currRow up/down
            
        return ''.join(rows)
        