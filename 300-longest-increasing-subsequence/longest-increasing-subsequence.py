class Solution(object):
    def lengthOfLIS(self, nums):
        a=[0]*len(nums);
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i]):
                    a[i]=max(a[i],1+a[j]);
        return max(a)+1;
        """
        :type nums: List[int]
        :rtype: int
        """
        