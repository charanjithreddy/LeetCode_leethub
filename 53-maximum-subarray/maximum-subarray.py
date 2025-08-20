class Solution(object):
    def maxSubArray(self, nums):
        res=-100000;
        t=0;
        for i in nums:
            if(i>t+i):
                t=i;
            else:
                t+=i;
            res=max(res,t);
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """