class Solution(object):
    def productExceptSelf(self, nums):
        pre=[];
        for i in range(len(nums)):
            if(i==0):
                pre.append(1);
            else:
                pre.append(pre[-1]*nums[i-1]);
        suf=[];
        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                suf.append(1);
            else:
                suf.append(suf[-1]*nums[i+1]);
        suf=suf[::-1];
        return [suf[i]*pre[i] for i in range(len(nums))];
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        