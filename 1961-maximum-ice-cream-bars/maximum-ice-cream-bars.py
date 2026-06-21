class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort();
        res=0;
        for i in costs:
            if(i<=coins):
                res+=1;
                coins-=i;
            else:
                break;
        return res
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        