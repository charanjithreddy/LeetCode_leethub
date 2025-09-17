class Solution(object):
    def merge(self, intervals):
        res=[];
        for [a,b] in intervals:
            new=[];
            curr=[a,b];
            for i in res:
                if(i[0]>b or i[1]<a):
                    new.append(i);
                else:
                    curr[0]=min(i[0],curr[0]);
                    curr[1]=max(i[1],curr[1]);
            new.append(curr);
            res=new;
        return res;
            
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        