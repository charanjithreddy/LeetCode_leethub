class Solution(object):
    def maxFrequencyElements(self, nums):
        m=1;
        d={};
        for i in nums:
            if(i in d):
                d[i]+=1;
                m=max(m,d[i]);
            else:
                d[i]=1;
        res=0;
        for i in d:
            if(d[i]==m):
                res+=m;
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """
        