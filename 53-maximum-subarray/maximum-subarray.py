class Solution(object):
    def maxSubArray(self, nums):
        res=float("-inf");
        t=0;
        for i in nums:
            if(t<0):
                t=i;
            else:
                t+=i;
            res=max(res,t);
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        