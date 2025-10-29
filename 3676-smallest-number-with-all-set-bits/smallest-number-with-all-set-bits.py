class Solution(object):
    def smallestNumber(self, n):
        l=len(bin(n)[2:]);
        return int("".join(["1"]*l),2);
        """
        :type n: int
        :rtype: int
        """
        