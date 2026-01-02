class Solution(object):
    def repeatedNTimes(self, nums):
        s=set()
        for i in nums:
            if(i in s):
                return i;
            else:
                s.add(i)
        """
        :type nums: List[int]
        :rtype: int
        """
        