class Solution(object):
    def insert(self, intervals, newInterval):
        o=[];
        for i in intervals:
            if(i[1]<newInterval[0] or i[0]>newInterval[1]):
                o.append(i);
            else:
                if(i[0]<newInterval[0]):
                    newInterval[0]=i[0];
                if(i[1]>newInterval[1]):
                    newInterval[1]=i[1];
        o.append(newInterval);
        o=sorted(o,key=lambda x:x[0]);
        return o;
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """