class Solution(object):
    def separateDigits(self, nums):
        res=[];
        for i in nums:
            res.extend([int(j) for j in str(i)]);
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        