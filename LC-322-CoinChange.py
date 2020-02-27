
class Solution:

    def coinChange(self, coins, amount):

        if not coins:
            return 0
        
        dp =[float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range()