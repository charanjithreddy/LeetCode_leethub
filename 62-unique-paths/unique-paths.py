class Solution(object):
    def uniquePaths(self, m, n):
        dp=[[0]*n for i in range(m)];
        dp[0][0]=1;
        for i in range(m):
            for j in range(n):
                if(i+1<m):
                    dp[i+1][j]+=dp[i][j]
                if(j+1<n):
                    dp[i][j+1]+=dp[i][j];
        return dp[m-1][n-1];
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        