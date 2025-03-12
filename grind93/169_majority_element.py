'''
Problem: Majority Element

Given an array 'nums' of size 'n', return the majority element.

The majority element is the element that appears more than '[n / 2]' times. You may 
assume that the majority element always exists in the array.

Example 1:

Input: nums=[3,2,3]
Output: 3

Example 2:

Input: nums=[2,2,1,1,1,2,2]
Output: 2
'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using Boyer-Moore Voting Algorithm
        
        count = 0
        candidate = None
        
        # find candidate for majority element
        for num in nums:
            if count == 0: # pick curr num as candidate
                candidate = num
                
            count += (1 if num == candidate else -1)
            
        return candidate
                
        
        
        # Naive solution uses O(n^2) time and O(1) space
        
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        
        # for i in range(n - 1):
        #     if nums.count(nums[i]) > (n // 2):
        #         return nums[i]
            
# Time Complexity: O(n)
# Space Complexity: O(1)

if __name__ == '__main__':
    sol = Solution()
    nums=[2,2,1,1,1,2,2]
    val = sol.majorityElement(nums)
    print(val)