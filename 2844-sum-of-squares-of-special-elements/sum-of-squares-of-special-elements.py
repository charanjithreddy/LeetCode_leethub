class Solution(object):
    def sumOfSquares(self, nums):
        res=0;
        n=len(nums)
        for i in range(n):
            if(n%(i+1)==0):
                res+=(nums[i]**2);
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        