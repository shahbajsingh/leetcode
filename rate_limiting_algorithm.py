'''
Problem: Rate-Limiting Algorithm

Some developers at Amazon are building a prototype for a simple rate-limiting algorithm. 
There are 'n' requests to be processed by the server, represented by a string 'requests', where 
the 'i'th character represents the region of the 'i'th client. Each request takes 1 unit of time to 
process.

There must be a minimum time gap of 'minGap' units between any two requests from the same region. 

    * The requests can be sent in any order, and there can be gaps in transmission for testing purposes.
    
    * Find the minimum amount of time required to process all the requests such that no request is denied.
    
Example 1:

Suppose n = 6, requests = 'aaabbb', and minGap = 2.

requests: a   a   a  b   b   b
            |   |      |   |
        a  b  __  a  b  __  a  b (minimum time gap of 2 between same region requests)

The requests can be sent in the order 'ab_ab_ab' where '_' represents that no request was sent in that unit
time. Here, the minimum time gap between two requests from the same region is 'minGap = 2'.

The total time taken is 8 units.

Example 2:

Input:
12
abacadaeafag
2

Explanation:
    * n = 12
    * requests = 'abacadaeafag'
    * minGap = 2
    
Sample Output:
16

Explanation:
One optimal strategy is 'ab_ad_afgae_ac_a'

Function Description:

Complete the function getMinTime in the editor:
    def getMinTime(n: int, requests: str, minGap: int) -> int:
    
Parameters:

    * n: the number of requests
    * requests: a string representing the region of each request
    * minGap: the minimum time gap required between requests from the same region
    
Returns:

    * an integer representing the minimum time required to process all requests without denial

'''

# PRIORITY QUEUE APPROACH

# use a priority queue to ensure that regions with more frequent 
# requests are processed at each time step

from collections import Counter, deque
import heapq

def getMinTime_priority_queue(n: int, requests: str, minGap: int) -> int:
    if not requests:
        return 0
    
    freq_map = Counter(requests) # count frequency of each region
    
    # create a max heap based on region frequency
    max_heap = [(-freq, region) for region, freq in freq_map.items()] # -freq to create max heap
    
    heapq.heapify(max_heap)
    
    # keep track of cooldown time for each region
    cooldown = deque() # (available_time, (-count, region))
    curr_time = 0 # current time step
    
    while max_heap or cooldown:
        curr_time += 1 # increment time step
        
        if max_heap:
            freq, region = heapq.heappop(max_heap) # get region with highest freq
            
            # process request
            freq += 1 # decrement freq (since freq is negative)
            
            if freq != 0:
                # add to cooldown deque
                cooldown.append((curr_time + minGap, (freq, region))) # (available_time, (-count, region))
                
        # check if any region is available to process
        if cooldown and cooldown[0][0] == curr_time:
            heapq.heappush(max_heap, cooldown.popleft()[1])
            
    return curr_time # return total time taken


# test function with the sample inputs
print('PROCESSING REQUESTS WITH PRIOIRTY QUEUE')
print(getMinTime_priority_queue(6, 'aaabbb', 2)) # 8
print(getMinTime_priority_queue(12, 'abacadaeafag', 2)) # 16




# SLIDING WINDOW APPROACH
    
# use a sliding window to ensure that no two requests from the same region
# are processed within minimum time gap

from collections import Counter, deque

def getMinTime_sliding_window(n: int, requests: str, minGap: int) -> int:
    if not requests:
        return 0
    
    # count frequency of each region
    freq_map = Counter(requests) 
    
    # initialize a deque for sliding window
    window = deque(maxlen=minGap)
    
    # keep track of total time taken
    time = 0
    
    while sum(freq_map.values()) > 0:
        # sort regions by remaining frequency in descending order
        sorted_regions = sorted(freq_map.items(), key=lambda x: -x[1])
        
        # find region not in window to process
        processed = False
        
        for region, freq in sorted_regions:
            if freq > 0 and region not in window:
                # process request
                freq_map[region] -= 1
                window.append(region)
                time += 1
                processed = True
                break
            
        if not processed: # no region to process
            # time gap
            window.append(None)
            time += 1
            
    return time # return total time taken

# test the function with the sample inputs
print('PROCESSING REQUESTS WITH SLIDING WINDOW')
print(getMinTime_sliding_window(6, 'aaabbb', 2)) # 8
print(getMinTime_sliding_window(12, 'abacadaeafag', 2)) # 16