class Solution(object):
    def findLHS(self, nums):
        d={};
        o=0;
        for i in nums:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        for i in d:
            if(i+1 in d):
                o=max(o,d[i]+d[i+1]);
        return o;
        """
        :type nums: List[int]
        :rtype: int
        """        