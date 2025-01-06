'''
Problem: Amazon Execute Processes (AWS Processor)

Amazon Web Services (AWS) has several processors for executing processes scheduled on 
its servers.

There are 'n' processes to be executed, where the 'i'th process takes execution[i] amount 
of time to execute. Two processes are cohesive if and only if their original execution times 
are equal. When a process with execution time execution[i] is executed, it takes execution[i] 
time to complete and simultaneously reduces the execution time of all its cohesive processes to 
ceil(execution[i] / 2).

Given the execution time of 'n' processes, find the total amount of time the processor takes to 
execute all the processes if you execute the processes in the given order, i.e. from left to right.

Notes

* The 'ceil()' function returns the smallest integer that is bigger or equal to its argument. For 
example, ceil(1.1) = 2, ceil(2.5) = 3, ceil(5) = 5, etc.

* If the execution time of some process 'i' is reduced and becomes equal to the execution time of 
any other process 'j', then the two processes 'i' and 'j' are not cohesive.

Function Description

Complete the function 'total_execution_time' with the following parameter:

* int execution[n]: an array of integers representing the execution times

Returns

* int: the total amount of time to execute all processes

Example 1

Input: execution = [5, 5, 3, 6, 5, 3]
Output: 21
Explanation:

processes 1, 2, and 5 are cohesive
processes 3, 6 are cohesive
process 4 is cohesive

Executing Process 1 results in [0, 3, 3, 6, 3, 3] // total_execution = 5
Executing Process 2 results in [0, 0, 3, 6, 2, 3] // total_execution = 8
Executing Process 3 results in [0, 0, 0, 6, 2, 2] // total_execution = 11
Executing Process 4 results in [0, 0, 0, 0, 2, 2] // total_execution = 17
Executing Process 5 results in [0, 0, 0, 0, 0, 2] // total_execution = 19
Executing Process 6 results in [0, 0, 0, 0, 0, 0] // total_execution = 21

Hence, total execution time is 21.
'''

from math import ceil
from typing import List
from collections import defaultdict

class Solution:
    def total_execution_time(self, execution: List[int]) -> int:
        n = len(execution)
        total_execution = 0
        
        # create two copies of execution list
        exec_orig = execution.copy()
        exec_curr = execution.copy()
        
        # map from execution time to indices
        exec_map = defaultdict(list)
        
        # iterate through execution list
        for i, exec_time in enumerate(execution):
            exec_map[exec_time].append(i)
        
        for i in range(n):
            if exec_curr[i] > 0: 
                _ = exec_curr[i] # store original execution time
                
                # execute process
                total_execution += exec_curr[i]
                exec_curr[i] = 0
                
                # update cohesive processes
                for j in exec_map[exec_orig[i]]:
                    if j != i and exec_curr[j] > 0:
                        # reduce execution time
                        exec_curr[j] = ceil(_ / 2)
                        
        return total_execution

# test cases
sol = Solution()
print(sol.total_execution_time([5, 5, 3, 6, 5, 3])) # 21