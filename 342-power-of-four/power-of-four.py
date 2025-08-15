class Solution(object):
    def isPowerOfFour(self, n):
        while(n>0):
            if(n==1 or n==4):
                return True;
            elif((n%100)%4!=0):
                return False;
            n/=4.0;
        return False;
        """
        :type n: int
        :rtype: bool
        """
        