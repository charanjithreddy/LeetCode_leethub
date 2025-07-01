class Solution(object):
    def productExceptSelf(self, nums):
        pre=[1];
        for i in range(1,len(nums)):
            pre.append(pre[-1]*nums[i-1]);
        suf=[1];
        for i in range(len(nums)-2,-1,-1):
            suf.append(suf[-1]*nums[i+1]);
        suf=suf[::-1];
        return [suf[i]*pre[i] for i in range(len(nums))];
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        