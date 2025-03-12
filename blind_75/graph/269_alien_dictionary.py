'''
Problem: Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order 
among the letters is unknown to you.

You are given a list of strings 'words' from the alien language's dictionary, 
where the strings in 'words' are sorted lexographically by the rules of this 
new language.

Return a string of the unique letters in the new alien language sorted in 
lexographically increasing order by the new language's rules. If there is 
no solution, return ''. If there are multiple solutions, return any of them.

Example 1:

Input: words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
Output: 'wertf'

Example 2:

Input: words = ['z', 'x']
Output: 'zx'

Example 3:

Input: words = ['z', 'x', 'z']
Output: ''
Explanation:

The order is invalid, so return ''.
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set) # adjacency list
        in_degree = {char: 0 for word in words for char in word} # in-degree for each node
        
        # build graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))
            
            # if word2 is prefix of word1 and shorter, order is invalid
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ''
            
            # find first non-matching char to establish an edge
            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j]) # add edge word1[j] -> word2[j]
                        in_degree[word2[j]] += 1 # increment in-degree of word2[j]
                    break
                
        # topological sort using Kahn's algorithm (BFS)
        # collect all nodes with no dependencies (in-degree 0)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        # process nodes with in-degree 0
        while queue:
            char = queue.popleft()
            result.append(char) # add to sorted order
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1 # remove edge char -> neighbor
                if in_degree[neighbor] == 0: # if no incoming edges, add to queue
                    queue.append(neighbor)
                    
                    
        # all nodes processed -> return result
        if len(result) == len(in_degree):
            return ''.join(result)
        
        # cycle exists -> no valid order
        return ''