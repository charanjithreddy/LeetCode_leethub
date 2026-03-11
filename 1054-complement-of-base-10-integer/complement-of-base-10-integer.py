class Solution(object):
    def bitwiseComplement(self, n):
        b=bin(n)[2:];
        return int("1"*len(b),2)-n
        """
        :type n: int
        :rtype: int
        """
        