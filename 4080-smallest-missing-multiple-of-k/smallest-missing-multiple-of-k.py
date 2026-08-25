class Solution(object):
    def missingMultiple(self, nums, k):
        nums=set(nums)
        t=k;
        while(t in nums):
            t+=k;
        return t
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        