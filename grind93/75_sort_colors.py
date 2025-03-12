'''
Problem: Sort Colors

Given an array 'nums' with 'n' objects colored red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, with colors in the order red, white, and blue.

We will use the integers '0', '1', and '2' to represent the color red, white, and blue respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums=[2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums=[2,0,1]
Output: [0,1,2]

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''
        Do not return anything, modify numbers in-place instead.
        '''
        # Dutch National Flag Algorithm
        
        # pointers for current, red (0), and blue (2) positions
        left, right = 0, len(nums) - 1
        curr = 0
        
        # process elements until curr pointer passes right pointer
        while curr <= right:
            if nums[curr] == 0: # red
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
                
            elif nums[curr] == 2: # blue
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            
            else: # white (1)
                curr += 1
                
        
# Time Complexity: O(n)
# Space Complexity: O(1)