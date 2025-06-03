class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort();
        d=nums[k-1]-nums[0];
        for i in range(k-1,len(nums)):
            x=nums[i]-nums[i-k+1];
            if(d>x):
                d=x;
        return d;
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """