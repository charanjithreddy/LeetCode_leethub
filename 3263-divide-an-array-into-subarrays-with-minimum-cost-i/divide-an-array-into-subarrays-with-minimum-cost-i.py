class Solution(object):
    def minimumCost(self, nums):
        return nums[0]+sum(sorted(nums[1:])[:2])
        """
        :type nums: List[int]
        :rtype: int
        """