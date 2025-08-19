class Solution(object):
    def zeroFilledSubarray(self, nums):
        def fact(n):
            if(n==0):
                return 0;
            else:
                t=0;
                for i in range(n,-1,-1):
                    t+=i;
                return t;
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
                res+=fact(cnt);
                cnt=0;
        res+=fact(cnt);
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """
        