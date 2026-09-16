class Solution(object):
    def maxProfit(self, prices):
        s=set();
        res=0;
        l=prices[0];
        for i in prices:
            res=max(res,i-l)
            l=min(l,i)
        return res
        """
        :type prices: List[int]
        :rtype: int
        """
        