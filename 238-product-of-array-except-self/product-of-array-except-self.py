class Solution(object):
    def productExceptSelf(self, nums):
        o=[1 for i in range(len(nums))];
        pre=1;
        for i in range(1,len(nums)):
            pre*=nums[i-1];
            o[i]*=pre;
        suf=1;
        for i in range(len(nums)-2,-1,-1):
            suf*=nums[i+1];
            o[i]*=suf;
        return o;


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        