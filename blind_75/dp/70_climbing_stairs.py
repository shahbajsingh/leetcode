'''
Problem: Climbing Stairs

You are climbing a staircase. It takes 'n' steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb 
to the top?

Example 1:

Input: n = 2
Output: 2
Explanation:

There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation:

There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # vars to store number of ways to reach
        # last two steps (n-1 and n-2) starting from 3
        one_step_before = 2 # 1 -> 2 -> 3  and  1 -> 3
        two_steps_before = 1 # 2 -> 3
        
        all_ways = 0 # var to store current number of ways
        
        for i in range(3, n + 1):
            # current number of ways is the sum of ways to reach
            # the previous step and the step before that
            all_ways = one_step_before + two_steps_before
            
            # update for next iteration
            two_steps_before = one_step_before # move one step up
            one_step_before = all_ways         # move to curr step
            
        return all_ways
    
sol = Solution()
print(sol.climbStairs(3))