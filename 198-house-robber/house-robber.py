class Solution(object):
    def rob(self, nums):
        if(len(nums)<3):
            return max(nums);
        else:
            m=0;
            for i in range(2,len(nums)):
                m=max(m,nums[i-2]);
                nums[i]=max(nums[i]+m,nums[i-1]);
        return nums[-1];
        """
        :type nums: List[int]
        :rtype: int
        """
        