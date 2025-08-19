class Solution(object):
    def zeroFilledSubarray(self, nums):
        res=0;
        if(0 not in nums):
            return res;
        cnt=0;
        for i in range(len(nums)):
            if(nums[i]==nums[i-1]==0):
                cnt+=1;
            elif(nums[i]==0):
                cnt=1;
            else:
                res+=((cnt*(cnt+1))/2);
                cnt=0;
        res+=((cnt*(cnt+1))/2);
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """