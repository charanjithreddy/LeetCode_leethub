class Solution(object):
    def insert(self, intervals, newInterval):
        res=[];
        for [a,b] in intervals:
            if(newInterval[0]>b or newInterval[1]<a):
                res.append([a,b]);
            else:
                newInterval[0]=min(newInterval[0],a);
                newInterval[1]=max(newInterval[1],b);
        res.append(newInterval);
        return sorted(res);
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        