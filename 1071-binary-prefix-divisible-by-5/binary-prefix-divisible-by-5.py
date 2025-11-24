class Solution(object):
    def prefixesDivBy5(self, nums):
        val=0;
        res=[];
        for i in nums:
            val=val*2+i;
            res.append(val%5==0);
        return res;
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        