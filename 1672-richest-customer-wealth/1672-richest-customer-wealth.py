class Solution(object):
    def maximumWealth(self, accounts):
        max=0;
        for i in range(len(accounts)):
            sum=0;
            for j in accounts[i]:
                sum+=j;
            if(i==0):
                max=sum;
                continue;
            if(sum>max):
                max=sum;
        return max;
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        