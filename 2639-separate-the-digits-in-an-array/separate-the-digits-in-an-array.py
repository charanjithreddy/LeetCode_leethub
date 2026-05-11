class Solution(object):
    def separateDigits(self, nums):
        res=[];
        for i in nums:
            t=[];
            while(i>0):
                t.append(i%10);
                i//=10;
            res.extend(t[::-1])
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        