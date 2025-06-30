class Solution(object):
    def findLHS(self, nums):
        d={};
        o=0;
        for i in nums:
            if(i-1 in d):
                if(i in d):
                    o=max(o,d[i-1]+d[i]+1);
                else:
                    o=max(o,d[i-1]+1);
            if(i+1 in d):
                if(i in d):
                    o=max(o,d[i+1]+d[i]+1);
                else:
                    o=max(o,d[i+1]+1);
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        return o;
        """
        :type nums: List[int]
        :rtype: int
        """
        