class Solution(object):
    def minPairSum(self, nums):
        nums.sort();
        res=nums[0]+nums[-1];
        for i in range(1,len(nums)//2):
            res=max(res,nums[i]+nums[-1-i]);
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """