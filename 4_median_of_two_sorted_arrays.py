'''
Problem: Median of Two Sorted Arrays

Given two sorted arrays 'nums1' and 'nums2' of size 'm' and 'n'
respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m + n)).

Example 1:

Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000
Explanation:

Merged array = [1, 2, 3] and median is 2

Example 2: 

Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.50000
Explanation:

Merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5

Constraints:

* nums1.length == m

* nums2.length == n

* 0 <= m <= 1000

* 0 <= n <= 1000

* 1 <= m + n <= 2000

* -10^6 <= nums1[i], nums2[i] <= 10^6
'''
from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge arrays
        merged = sorted(nums1 + nums2)
        
        # calculate length merged array
        n = len(merged)
        
        # calculate median
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]