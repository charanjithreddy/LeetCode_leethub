class Solution(object):
    def missingNumber(self, nums):
        n=max(nums);
        s=sum(nums);
        a=n*(n+1)/2;
        if(a-s==0):
            if(0 in nums):
                return n+1;
            else:
                return 0;
        return a-s;
        """
        :type nums: List[int]
        :rtype: int
        """
        