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
        return list(d.values()).count(m)*m;
        """
        :type nums: List[int]
        :rtype: int
        """
        