class Solution(object):
    def minPairSum(self, nums):
        nums.sort();
        o=0;
        n=len(nums)/2;
        for i in range(n):
            if(o<(nums[i]+nums[len(nums)-i-1])):
                o=nums[i]+nums[len(nums)-i-1];
        return o;

        """
        :type nums: List[int]
        :rtype: int
        """
        