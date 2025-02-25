'''
Problem: Coin Change

You are given an integer array 'coins' representing coins of different denominations 
and an integer 'amount' representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount 
of money cannot be made up by any combination of coins, return '-1'.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation:

11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 'i'th element of dp array -> fewest coins to make 'i'th amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1): # iterate to target amount
            for coin in coins: # try each coin
                if i >= coin: # if coin can be used
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != float('inf') else -1
    
sol = Solution()
print(sol.coinChange([1,2], 11))