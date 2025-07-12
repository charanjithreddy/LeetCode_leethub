class Solution(object):
    def isHappy(self, n):
        s=set();
        while(n>=1):
            if(n==1):
                return True;
            t=0;
            while(n>0):
                t+=(n%10)**2;
                n//=10;
            if(t in s):
                return False;
            s.add(t);
            n=t;
        return n==1;
        """
        :type n: int
        :rtype: bool
        """