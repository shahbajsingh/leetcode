'''
Problem: Merge Intervals

Given an array 'intervals' where 'intervals[i] = [start_i, end_i]', merge all overlapping 
intervals, and return an array of the non-overlapping intervals that cover all the intervals 
in the input.

Example 1:

Input: intervals=[[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation:

Since intervals [1,3] and [2,6] overlap, merge them into [1,6]

Example 2:

Input: intervals=[[1,4],[4,5]]
Output: [[1,5]]
Explanation: 

Intervals [1,4] and [4,5] are considered overlapping
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # base case
        if not intervals: 
            return []
        
        # sort intervals by 'start_i'
        intervals.sort(key=lambda x: x[0])
        
        merged = [] # store merged intervals
        
        for interval in intervals:
            # if merged arr is empty or curr interval does not overlap with previous
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                
            else: 
                # merge intervals by updating 'end_i' of previous interval
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)

if __name__ == '__main__':
    sol = Solution()
    intervals=[[1,3],[2,6],[8,10],[15,18]]
    val = sol.merge(intervals)
    print(val)
    