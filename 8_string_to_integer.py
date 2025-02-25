'''
Problem: String to Integer (atoi)

Implement the 'myAtoi(string s)' function, which converts a string to a 32-bit signed 
integer.

The algorithm for 'myAtoi(string s)' is as follows:

1. Whitespace: Ignore any leading whitespace (' ')

2. Signedness: Determine the sign by checking if the next character is '-' or '+', 
assuming positivity if neither is present.

3. Conversion: Read the itneger by skipping leading zeros until a non-digit character 
is encountered or the end of the string is reached. If no digits were read, then the 
result is 0.

4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], 
then round the integer to remain in the range. Specifically, integers less than -2^31 
should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 
2^31 - 1.

Return the integer as the final result.

Example 1:

Input: s = '42'
Output: 42
Explanation:

The underlined characters are what is read in and the caret is the current reader 
position.

Step 1:    "42" (no characters read because there is no leading whitespace)
            ^
Step 2:    "42" (no characters read because there is neither a '-' nor '+')
            ^
Step 3:    "42" ("42" is read in)
            __^
            
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1:    "   -042" (leading whitespace is read and ignored)
            ___^
Step 2: "   -042" ('-' is read, so the result should be negative)
            _^
Step 3: "  -042" ("042" is read in, leading zeros ignored in the result)
            __^

Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1:    "1337c0d3" (no characters read because there is no leading whitespace)
            ^
Step 2:    "1337c0d3" (no characters read because there is neither a '-' nor '+')
            ^
Step 3:    "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
            ___^

Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1:    "0-1" (no characters read because there is no leading whitespace)
            ^
Step 2:    "0-1" (no characters read because there is neither a '-' nor '+')
            ^
Step 3:    "0-1" ("0" is read in; reading stops because the next character is a non-digit)
            _^

Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.


'''
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # remove leading whitespace
        n = len(s)
        i = 0
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n: # string is empty
            return 0
            
        # check for optional sign
        sign = 1
            
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
                
        # convert string to integer
        num = 0
            
        while i < n and s[i].isdigit():
            digit = int(s[i])
                
            # check for overflow
            if num > INT_MAX // 10 or \
                (num == INT_MAX // 10 and digit > 7):
                    return INT_MAX if sign == 1 else INT_MIN
                    
            # update number
            num = num * 10 + digit
            i += 1
                
        # apply sign
        return sign * num