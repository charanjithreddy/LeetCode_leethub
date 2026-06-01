class Solution(object):
    def minimumCost(self, cost):
        i=1;
        cost.sort(reverse=True);
        res=0;
        for candy in cost:
            if(i%3==0):
                i+=1
                continue;
            res+=candy;
            i+=1;
        return res

        """
        :type cost: List[int]
        :rtype: int
        """
        