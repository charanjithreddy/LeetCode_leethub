class Solution(object):
    def isHappy(self, n):
        while(n>6):
            t=0;
            while(n>0):
                t+=(n%10)**2;
                n//=10;
            n=t;
        return n==1;

        """
        :type n: int
        :rtype: bool
        """
        