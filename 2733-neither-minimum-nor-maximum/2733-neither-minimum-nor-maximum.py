class Solution(object):
    def findNonMinOrMax(self, nums):
        for i in nums:
            if (i!=min(nums) and i!=max(nums)):
                return i;
        return -1;