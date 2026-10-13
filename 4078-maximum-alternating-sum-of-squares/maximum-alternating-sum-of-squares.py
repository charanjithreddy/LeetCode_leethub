class Solution(object):
    def maxAlternatingSum(self, nums):
        nums=[i**2 for i in nums];
        nums.sort();
        res=-1*sum(nums[:len(nums)//2])+sum(nums[len(nums)//2:])
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        