class Solution(object):
    def coinChange(self, coins, amount):
        dp=[-1]*(amount+1)
        dp[0]=0;
        coins.sort()
        for i in range(len(dp)):
            for j in coins:
                if(i+j>=len(dp)):
                    break
                if(dp[i+j]==-1 and dp[i]!=-1):
                    dp[i+j]=dp[i]+1;
                elif(dp[i]!=-1):
                    dp[i+j]=min(dp[i+j],dp[i]+1);
        return dp[amount]
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        