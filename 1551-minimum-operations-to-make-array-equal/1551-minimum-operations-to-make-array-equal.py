class Solution(object):
    def minOperations(self, n):
        s=0;
        for i in range(n/2):
            s+=(n-1-(2*i));
        return s;
        """
        :type n: int
        :rtype: int
        """
        