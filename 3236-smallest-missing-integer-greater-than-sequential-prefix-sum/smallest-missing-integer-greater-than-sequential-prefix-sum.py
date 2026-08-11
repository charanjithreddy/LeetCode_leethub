class Solution(object):
    def missingInteger(self, nums):
        res=nums[0];
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
                res+=nums[i];
            else:
                break;
        while res in nums:
            res+=1;
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        