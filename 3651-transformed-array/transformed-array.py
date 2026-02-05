class Solution(object):
    def constructTransformedArray(self, nums):
        n=len(nums);
        res=[];
        for i in range(len(nums)):
            if(nums[i]>0):
                res.append(nums[(i+nums[i])%n]);
            elif(nums[i]<0):
                res.append(nums[(i+nums[i]+n)%n]);
            else:
                res.append(nums[i]);
        return res;
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        