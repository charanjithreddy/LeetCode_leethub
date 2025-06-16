class Solution(object):
    def maximumDifference(self, nums):
        o=-1;
        mi=nums[0];
        for i in range(1,len(nums)):
            if(nums[i]>mi):
                o=max(o,nums[i]-mi);
            
            if(nums[i]<mi):
                mi=nums[i];
        return o;
        """
        :type nums: List[int]
        :rtype: int
        """
        