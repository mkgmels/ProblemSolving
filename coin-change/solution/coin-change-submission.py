class Solution:
    def coinChange(self, coins, amount):
        dp=[float("inf") for _ in range(amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],1+dp[i-coin])
        return dp[amount] if not dp[amount]==float('inf') else -1


        
