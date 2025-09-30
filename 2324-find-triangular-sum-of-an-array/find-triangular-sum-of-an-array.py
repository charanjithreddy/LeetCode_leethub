class Solution(object):
    def triangularSum(self, nums):
        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                nums[j]+=nums[j+1];
        return nums[0]%10;

        """
        :type nums: List[int]
        :rtype: int
        """
        