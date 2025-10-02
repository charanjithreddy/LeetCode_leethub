class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        res=0;
        empty=0;
        while(numBottles>0):
            res+=numBottles;
            empty+=numBottles;
            numBottles=0;
            while(empty>=numExchange):
                numBottles+=1;
                empty-=numExchange;
                numExchange+=1;
        return res;
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        