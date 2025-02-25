'''
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without 
duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation:

The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation:

The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation:

The answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a 
subsequence and not a substring.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        res = 0
        char_set = set() # set to store unique chars
        l = 0 # left ptr
        
        for r, c in enumerate(s): # right ptr and char
            while c in char_set: # if char already in set
                char_set.remove(s[l]) # remove char from set
                l += 1
            char_set.add(c) # add char to set
            res = max(res, r - l + 1) 
            
        return res
        