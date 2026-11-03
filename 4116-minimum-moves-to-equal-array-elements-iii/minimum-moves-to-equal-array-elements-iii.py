class Solution(object):
    def minMoves(self, nums):
        m=max(nums);
        res=[m-i for i in nums]
        return sum(res)
        """
        :type nums: List[int]
        :rtype: int
        """
        