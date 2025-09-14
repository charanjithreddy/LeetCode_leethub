class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m=len(text1);
        n=len(text2);
        dp=[[0]*(n+1) for i in range(m+1)];
        for i in range(m):
            for j in range(n):
                if(text1[i]==text2[j]):
                    dp[i+1][j+1]=dp[i][j]+1;
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1]);
        return dp[m][n];

        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        