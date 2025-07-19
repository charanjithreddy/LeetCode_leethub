class Solution(object):
    def findDuplicate(self, nums):
        for i in nums:
            x=abs(i);
            if(nums[x]<0):
                return x;
            nums[x]*=-1;
        """
        :type nums: List[int]
        :rtype: int
        """