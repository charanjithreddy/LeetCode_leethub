class Solution(object):
    def findMaxAverage(self, nums, k):
        t=0.0;
        for i in range(k):
            t+=nums[i];
        res=t/k
        for i in range(k,len(nums)):
            t+=nums[i];
            t-=nums[i-k];
            res=max(res,t/k);
        return res;
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """