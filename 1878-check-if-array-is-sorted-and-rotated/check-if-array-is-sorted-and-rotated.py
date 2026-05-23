class Solution(object):
    def check(self, nums):
        n=len(nums);
        t=sorted(nums);
        for i in range(n):
            nums=nums[-1:]+nums[:-1];
            if(nums==t):
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        