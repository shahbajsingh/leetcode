'''
Problem: Longest Increasing Subsequence

Given an integer array 'nums', return the length of the longest strictly increasing 
subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation:

The longest increasing subsequence is [2,3,7,101]

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''
from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n # dp[i] is the LIS at i
        
        for i in range(n):
            # compare nums[i] with all previous elements nums[j]
            for j in range(i):
                if nums[i] > nums[j]: # if nums[i] can extent LIS ending at nums[j]
                    dp[i] = max(dp[i], dp[j] + 1) # update dp[i]
                    
        return max(dp)
    
    def lengthOfLIS_optimized(self, nums: List[int]) -> int:
        sub = [] # will store smallest tail
        
        for num in nums:
            # find the index to replace in 'sub' using binary search
            i = bisect.bisect_left(sub, num)
            
            # if num is greater than all elements in 'sub'
            if i == len(sub): # where num can be inserted without breaking order
                sub.append(num) # append
            else: # if num can replace an element in 'sub'
                sub[i] = num # update smallest tail for subsequence
                
        return len(sub)
    
if __name__ == '__main__':
    sol = Solution()
    res = sol.lengthOfLIS_optimized([10,9,2,5,3,7,101,18])
    print(res)
