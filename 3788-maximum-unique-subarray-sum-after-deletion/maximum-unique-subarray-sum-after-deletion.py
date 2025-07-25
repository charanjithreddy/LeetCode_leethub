class Solution(object):
    def maxSum(self, nums):
        if(max(nums)<0):
            return max(nums)
        s=set();
        o=0;
        for i in nums:
            if(i>0 and i not in s):
                o+=i;
                s.add(i);
        return o;

        """
        :type nums: List[int]
        :rtype: int
        """
        