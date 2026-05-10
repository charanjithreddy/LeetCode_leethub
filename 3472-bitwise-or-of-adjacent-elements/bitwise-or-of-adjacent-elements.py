class Solution(object):
    def orArray(self, nums):
        res=[];
        for i in range(len(nums)-1):
            res.append(nums[i]|nums[i+1])
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        