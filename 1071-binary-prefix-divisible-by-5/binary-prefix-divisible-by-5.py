class Solution(object):
    def prefixesDivBy5(self, nums):
        res=[nums[0]%5==0];
        for i in range(1,len(nums)):
            nums[i]=(nums[i-1]*2+nums[i])%5;
            res.append(nums[i]%5==0);
        return res;
        """
        :type nums: List[int]
        :rtype: List[bool]
        """