class Solution(object):
    def xorOperation(self, n, start):
        o=start;
        for i in range(1,n):
            o^=start+2*i
        return o;
        """
        :type n: int
        :type start: int
        :rtype: int
        """