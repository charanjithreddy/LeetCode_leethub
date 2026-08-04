class Solution(object):
    def findMissingElements(self, nums):
        s=set(nums);
        res=[];
        for i in range(min(s),max(s)+1):
            if(i not in s):
                res.append(i);
        return sorted(res)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        