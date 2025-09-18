class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals,key=lambda x: x[0]);
        res=[intervals[0]];
        for i in intervals[1:]:
            if(i[0]>res[-1][1]):
                res.append(i);
            else:
                res[-1][0]=min(res[-1][0],i[0]);
                res[-1][1]=max(res[-1][1],i[1]);
        return res;
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        