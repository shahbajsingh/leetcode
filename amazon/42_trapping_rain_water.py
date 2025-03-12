'''
Problem: Trapping Rain Water

Given 'n' non-negative integers representing an elevation map where the width of each 
bar is '1', compute how much water it can trap after raining.

Example 1:

Input: height=[0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation:

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this 
case, 6 units of rain water are being trapped.

Example 2:

Input: height=[4,2,0,3,2,5]
Output: 9
'''
from typing import List

class Solution:
    # TWO-POINTER APPROACH
    def trap(self, height: List[int]) -> int:
        # base case
        if not height:
            return 0
        
        left_ptr, right_ptr = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0
        
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                # if curr height is greater than left_max, update it
                if height[left_ptr] >= left_max:
                    left_max = height[left_ptr]
                    
                else: # water trapped = diff between curr height and left_max
                    total_water += left_max - height[left_ptr]
                    
                left_ptr += 1 # increment left pointer
                
            else: # height is greater at left pointer than at right pointer
                # if curr height is greater than right_max, update it
                if height[right_ptr] >= right_max:
                    right_max = height[right_ptr]
                
                else: # water trapped = diff between curr height and right_max
                    total_water += right_max - height[right_ptr]
                    
                right_ptr -= 1 # decrement right pointer
                
        return total_water
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
    
    # DYNAMIC PROGRAMMING APPROACH
    def trap(self, height: List[int]) -> int:
        # base case
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n # arr to store max height from left at each index
        right_max = [0] * n # arr to store max height from right at each index
        total_water = 0
        
        # fill left_max with max heights from the left
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            
        # fill right_max with max heights from the right
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        # calculate trapped water with precomputed max heights
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]
            
        return total_water
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)