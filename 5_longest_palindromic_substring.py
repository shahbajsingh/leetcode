'''
Problem: Given a string 's', return the longest palindromic 
substring in 's'.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s or n == 0: # empty string
            return ''
        
        start, end = 0, 0 # palindrome left and right ptr
        
        def expandAroundCenter(l: int, r: int) -> int:
            while l >= 0 and r < n and s[l] == s[r]: # char matching
                l -= 1
                r += 1
                
            return r - l - 1 # step back
        
        for i in range(n):
            odd = expandAroundCenter(i, i) # check odd len palindrome
            even = expandAroundCenter(i, i+1) # check even len palindrome
            max_len = max(odd, even)
            
            if max_len > end - start: # expand ptrs half len each direction
                start = i - (max_len - 1) // 2
                end = i + max_len // 2 + 1
                
        return s[start:end]
            
            
        