class Solution(object):
    def minimumOperations(self, nums):
        res=0;
        for i in nums:
            if(i%3!=0):
                res+=1;
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """