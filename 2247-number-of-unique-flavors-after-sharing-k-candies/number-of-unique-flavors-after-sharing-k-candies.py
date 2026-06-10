class Solution(object):
    def shareCandies(self, candies, k):
        d={};
        for i in candies[k:]:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        res=len(d);
        for i in range(len(candies)-k):
            if(candies[i] in d):
                d[candies[i]]+=1;
            else:
                d[candies[i]]=1;
            d[candies[i+k]]-=1;
            if(d[candies[i+k]]==0):
                del d[candies[i+k]];
            res=max(res,len(d))
        return res
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """