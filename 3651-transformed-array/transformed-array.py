class Solution(object):
    def constructTransformedArray(self, nums):
        n=len(nums);
        res=[0]*n;
        for i in range(len(nums)):
            if(nums[i]>0):
                res[i]=(nums[(i+nums[i])%n]);
            elif(nums[i]<0):
                res[i]=(nums[(i+nums[i]+n)%n]);
            else:
                res[i]=(nums[i]);
        return res;
        """
        :type nums: List[int]
        :rtype: List[int]
        """