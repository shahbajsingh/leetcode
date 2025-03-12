'''
Problem: Course Schedule

There are a total of 'numCourses' courses you have to take, labeled from '0' to 
'numCourses - 1'. You are given an array 'prerequisites' where 'prerequisites[i] = 
[a_i, b_i]' indicates that you must take course 'b_i' first if you want to take 
course 'a_i'.

Return true if you can finish all courses. Otherwise, return 'false'.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation:

There are a total of 2 courses to take. To take course 1 you should have finished 
course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: 

There are a total of 2 courses to take. To take course 1 you should have finished 
course 0, and to take course 0 you should have finished course 1. So it is impossible.
'''
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize adjacency list and in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        # build graph and count in-degrees
        for a, b in prerequisites:
            graph[b].append(a) # b -> a (b is a prereq for a)
            in_degree[a] += 1 # edge going into a
            
        # add no prereq courses (0 in-degrees) to queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0 # track possible courses
        
        # process course nodes with BFS
        while queue:
            course = queue.popleft() # get next course with no prereqs
            count += 1
            
            # reduce in-degree for neighbors (for which this course is a prereq)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                
                # if in-degree becomes 0, add to queue (course can now be taken)
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                        
        # check if all courses can be taken (no cycles)
        return count == numCourses