class Solution(object):
    def minimumCost(self, nums):
        i=nums[0];
        return i+sum(sorted(nums[1:])[:2])

        """
        :type nums: List[int]
        :rtype: int
        """
        