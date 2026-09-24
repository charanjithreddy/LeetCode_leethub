class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if(i==sum([int(x) for x in str(nums[i])])):
                return i;
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        