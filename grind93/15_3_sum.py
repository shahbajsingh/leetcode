'''
Problem: 3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the output 
and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation:

The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0,
Output: [[0,0,0]]
Explanation:

The only possible triplet sums up to 0.

Constraints:

* 3 <= nums.length <= 3000
* -10^5 <= nums[i] <= 10^5
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array 
        nums.sort()
        
        result = []
        n = len(nums)
        
        for i in range(n):
            # check for duplicates
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            
            # initialize left and right ptrs
            left, right = i + 1, n - 1
            
            # iterate the array for sums
            while (left < right):
                # calculate sum
                sum = nums[i] + nums[left] + nums[right]
                
                # check sum and append
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # skip duplicates for both pointers
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1
                    
                # if sum is too small
                elif (sum < 0):
                    left += 1 # increment left ptr
                    
                # if sum is too large
                else: # (sum > 0)
                    right -= 1 # decrement right ptr
                    
        return result 
            
# Time Complexity: O(n^2)
# Space Complexity: O(n) 