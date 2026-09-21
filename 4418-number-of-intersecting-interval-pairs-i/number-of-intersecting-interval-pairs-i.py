class Solution(object):
    def countIntersectingIntervals(self, intervals):
        res=0;
        for i in range(len(intervals)):
            starti,endi=intervals[i];
            for j in range(i+1,len(intervals)):
                startj,endj=intervals[j];
                if(max(starti,startj)<=min(endi,endj)):
                    res+=1;
        return res

                
        
        """
        :type intervals: List[List[int]]
        :rtype: int
        """