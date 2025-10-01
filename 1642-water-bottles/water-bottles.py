class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        empty=0;
        res=0;
        while(numBottles>0):
            res+=numBottles;
            empty+=numBottles;
            numBottles=empty//numExchange;
            empty=empty%numExchange;
        return res;
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        