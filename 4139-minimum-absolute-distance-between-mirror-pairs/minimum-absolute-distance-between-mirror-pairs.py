class Solution(object):
    def minMirrorPairDistance(self, nums):
        res=-1;
        d={};
        for i in range(len(nums)-1,-1,-1):
            s=str(nums[i])[::-1];
            while(s[0]=="0"):
                s=s[1:];
            if(int(s) in d):
                if(res==-1):
                    res=abs(i-d[int(s)]);
                else:
                    res=min(res,abs(i-d[int(s)]));
            d[nums[i]]=i;
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        