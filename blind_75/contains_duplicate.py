'''
Problem: Contains Duplicate

Given an integer array 'nums', return 'true' if any value appears at least twice in 
the array, and return 'false' if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation:

All elements are distinct

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Contraints:

* 1 <=nums.length <= 10^5

* -10^9 <= nums[i] <= 10^9

'''

from typing import List

class Solution(object):
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) # set() removes duplicates
    
# TIME COMPLEXITY: O(n)

# test cases
sol = Solution()
print(sol.contains_duplicate([1, 2, 3, 1])) # True
print(sol.contains_duplicate([1, 2, 3, 4])) # False
print(sol.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # True