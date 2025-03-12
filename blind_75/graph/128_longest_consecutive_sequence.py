'''
Problem: Longest Consecutive Sequence

Given an unsorted array of integers 'nums', return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation:

The longest consecutive elements sequence is [1,2,3,4]

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:

Input: nums = [1,0,1,2]
Output: 3
'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case
        if not nums:
            return 0
        
        # convert list to set for O(1) lookup
        num_set = set(nums)
        longest_seq = 0 # longest sequence length
        
        for num in num_set:
            if num - 1 not in num_set: # num must start sequence
                curr_num = num
                curr_seq = 1 # current sequence length
                
                while curr_num + 1 in num_set: # iterate sequence
                    curr_num += 1
                    curr_seq += 1
                    
                longest_seq = max(longest_seq, curr_seq) # update
                
        return longest_seq