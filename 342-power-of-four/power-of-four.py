class Solution(object):
    def isPowerOfFour(self, n):
        while(n>0):
            if(n==1):
                return True;
            n/=4.0;
        return False;
        """
        :type n: int
        :rtype: bool
        """
        