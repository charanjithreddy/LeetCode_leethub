class Solution(object):
    def maxProfit(self, prices):
        profit=0;
        b=prices[0];
        s=prices[0];
        for i in prices:
            if(i<b):
                profit=max(profit,s-b);
                b=i;
                s=i;
            elif(i>s):
                s=i;
        return max(profit,s-b);

        """
        :type prices: List[int]
        :rtype: int
        """
        