'''
Problem: Two Sum

Given an array of integers 'nums' and an integer 'target', return indices of the two 
numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:

Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:

* 2 <= nums.length <= 10^4

* -10^9 <= nums[i] <= 10^9

* -10^9 <= target <= 10^9

* Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary to store index of numbers
        num_dict = {}
        
        # iterate through list
        for i, num in enumerate(nums):
            # calculate difference between target and number
            diff = target - num
            
            # if difference in dictionary, return indices
            if diff in num_dict:
                return [num_dict[diff], i]
            
            # add number to dictionary
            num_dict[num] = i
            
        return []
    
# TIME COMPLEXITY: O(n)

# test cases
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(sol.twoSum([3, 2, 4], 6)) # [1, 2]
print(sol.twoSum([3, 3], 6)) # [0, 1]
        