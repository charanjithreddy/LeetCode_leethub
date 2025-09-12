class Solution(object):
    def lengthOfLIS(self, nums):
        a=[1]*len(nums);
        res=1;
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i]):
                    a[i]=max(a[i],1+a[j]);
            res=max(res,a[i]);
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """