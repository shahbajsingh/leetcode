'''
Problem: Max Transfer Rate

You are in the Amazon Cloud Infrastructure Team, and you are working on a project to optimize how 
data flows through its network of storage servers.

You are given 'n' storage servers, and the throughput capacity of each server is given in an integer 
array named 'throughput'.

There are 'pipeline_count' data pipelines that need to be connected to two storage servers, one as the 
primary connection and the other as the backup. Each data pipeline must choose a unique pair of servers for 
its connections.

The 'transfer_rate' for each data pipeline is defined as the sum of the throughput of its primary and 
backup servers.

Given an integer array 'throughput' and an integer 'pipeline_count', find the maximum total 'transfer_rate' 
that can be obtained by optimally choosing unique pairs of connections for each data pipeline.

Note:

A pair of servers (x, y) is said to be unique if no other pipeline has selected the same pair. However, 
the pairs (y, x) and (x, y) are treated as different connections. 

It is also possible to select the same server for primary and backup connections, which means that (x, x) 
is a valid pair of connections.

Function Description

Complete the function max_transfer_rate, which has the following parameter(s):

1.int throughput[n]: an array of throughput provided by each server instance.

2. int pipeline_count: the number of data pipelines that need to be connected.

Returns

int: the maximum total transfer rate

Example 1:

Input: throughput = [4, 2, 5], pipeline_count = 4
Output: 36
Explanation:

The data pipelines can select their connection among the following 9 possible server pairs
(Assuming 1-based indexing of throughput array):

[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]

To achieve the maximum total transfer_rate, the data pipelines can optimally choose the pairs 
[3, 3], [1, 3], [3, 1], [1, 1] to obtain the maximum sum of transfer_rate = 
(5 + 5) + (5 + 4) + (4 + 5) + (4 + 4) = 36.

'''
from typing import List

def max_transfer_rate(throughput: List[int], pipeline_count: int) -> int:
    n = len(throughput)
    
    # total possible unique pairs (x, y) where 0 <= x, y < n
    total_pairs = n * n
    
    # adjust pipeline_count to be at most total_pairs
    pipeline_count = min(pipeline_count, total_pairs)
    
    # list to store transfer rates
    transfer_rates = []
    
    # generate all possible pairs of servers and calculate transfer rates
    for x in range(n):
        for y in range(n):
            transfer_rate = throughput[x] + throughput[y]
            transfer_rates.append(transfer_rate)
    
    # sort transfer_rates in descending order
    transfer_rates.sort(reverse=True)
    
    # select the first pipeline_count transfer rates
    top_transfer_rates = transfer_rates[:pipeline_count]
    
    # calculate total transfer rate
    total_transfer_rate = sum(top_transfer_rates)
    
    return total_transfer_rate

# test solution with sample test cases
print(max_transfer_rate([4, 2, 5], 4)) # 36
    