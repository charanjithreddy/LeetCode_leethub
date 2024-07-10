class Solution(object):
    def buildArray(self, nums):
        o=[];
        for i in range(len(nums)):
            o.append(nums[nums[i]]);
        return o;
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        