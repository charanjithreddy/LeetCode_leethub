class Solution(object):
    def search(self, nums, target):
        if target in nums:
            for i in range(0,len(nums)):
                if nums[i]==target:
                    return i;
                    
        else:
            return -1;
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        