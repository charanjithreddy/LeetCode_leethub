class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        output=0;
        for i in range(len(nums)):
            if(str(bin(i))[2::].count("1")==k):
                output+=nums[i];
        return output;
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        