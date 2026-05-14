class Solution(object):
    def isGood(self, nums):
        d={};
        m=max(nums);
        for i in nums:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        for i in range(1,m+1):
            if(i not in d):
                return False
            d[i]-=1;
            if(d[i]<0):
                return False;
        d[m]-=1;
        l=set(list(d.values()))
        return l==set([0])
        """
        :type nums: List[int]
        :rtype: bool
        """
        