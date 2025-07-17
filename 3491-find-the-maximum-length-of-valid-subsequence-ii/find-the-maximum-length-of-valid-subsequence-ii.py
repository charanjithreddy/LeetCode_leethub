class Solution(object):
    def maximumLength(self, nums, k):
        dp=[];
        for i in range(k):
            a=[];
            for i in range(k):
                a.append([]);
            dp.append(a);
        for i in nums:
            index=i%k;
            for j in range(k):
                if(dp[index][j]==[]):
                    dp[index][j].append(i);
                elif(j==index):
                    dp[index][j].append(i);
                elif(dp[index][j][-1]%k==j):
                    dp[index][j].append(i);
            for j in range(k):
                if(j!=index and dp[j][index]!=[] and dp[j][index][-1]%k==j):
                    dp[j][index].append(i);
        o=0;
        for i in dp:
            for j in i:
                o=max(o,len(j));
        return o;
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        