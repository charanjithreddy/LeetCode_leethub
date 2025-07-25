class Solution(object):
    def maxSum(self, nums):
        if(max(nums)<0):
            return max(nums)
        return sum(set([i for i in nums if i>0]));
        """
        :type nums: List[int]
        :rtype: int
        """