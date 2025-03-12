'''
Problem: LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the 'LRUCache' class:

* 'LRUCache(int capacity)': initialize the LRU cache with positive size 'capacity'

* 'int get(int key)': return the value of the 'key' if the key exists, otherwise return -1

* 'void put(int key, int value)': update the value of the 'key' if the 'key' exists. Otherwise, 
add the 'key-value' pair to the cache. If the number of keys exceeds the 'capacity' from this 
operation, evict the least recently used key.

The functions 'get' and 'put' must each run in O(1) average time complexity:

Example 1:

Input: 
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''
from collections import OrderedDict

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self. value = value
        self.prev = None
        self.next = None

class LRUCache:
    # with doubly linked list and hashmap
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # hashmap to store key -> node
        self.head = Node(0, 0) # dummy head
        self.tail = Node(0, 0) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: Node):
        '''Remove node from doubly linked list'''
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _add_to_end(self, node: Node):
        '''Add node to end (MRU) position'''
        prev_last = self.tail.prev
        prev_last.next = node
        node.prev = prev_last
        node.next = self.tail
        self.tail.prev = node
        
    def get(self, key:int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            # remove from curr position and add to end (MRU) position
            self._remove(node)
            self._add_to_end(node)
            return node.value
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update node value and move to end (MRU) position
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_end(node)
            
        else:
            if len(self.cache) >= self.capacity:
                # remove LRU node (first real node after head)
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key] # evict from hashmap
                
            # insert new node at end (MRU) position
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_end(new_node)
    
    # with OrderedDict
    
    # def __init__(self, capacity: int):
    #     self.cache = OrderedDict()
    #     self.capacity = capacity
        
    # def get(self, key: int) -> int:
    #     if key not in self.cache:
    #         return -1
        
    #     # move accessed key to end to mark as MRU
    #     self.cache.move_to_end(key)
    #     return self.cache[key]
        
    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         # move to end to mark as MRU
    #         self.cache.move_to_end(key)
    #     self.cache[key] = value # update value of key

    #     if len(self.cache) > self.capacity:
    #         # remove LRU key
    #         self.cache.popitem(last=False)
        
# TC and SC for both methods
# Time Complexity: O(1)
# Space Complexity: O(capacity)