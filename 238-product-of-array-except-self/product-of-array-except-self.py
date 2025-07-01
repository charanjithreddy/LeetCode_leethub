class Solution(object):
    def productExceptSelf(self, nums):
        o=[1 for i in nums];
        x=1;
        for i in range(1,len(nums)):
            x*=nums[i-1];
            o[i]*=x;
        x=1;
        for i in range(len(nums)-2,-1,-1):
            x*=nums[i+1];
            o[i]*=x;
        return o;


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        