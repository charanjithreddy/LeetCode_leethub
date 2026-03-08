class Solution(object):
    def findDifferentBinaryString(self, nums):
        n=len(nums);
        for i in range(2**n):
            b=bin(i)[2:];
            b="0"*(n-len(b))+b
            if(b not in nums):
                return b
        """
        :type nums: List[str]
        :rtype: str
        """
        