class Solution(object):
    def candy(self, ratings):
        o=[1]*len(ratings);
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                o[i]=o[i-1]+1;
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i]>ratings[i+1]):
                if(o[i]<=o[i+1]):
                    o[i]=o[i+1]+1;
        return sum(o);
        """
        :type ratings: List[int]
        :rtype: int
        """