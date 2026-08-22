class Solution(object):
    def checkDivisibility(self, n):
        s=0;
        p=1;
        t=n;
        while(t>0):
            s+=t%10;
            p*=t%10;
            t//=10;
        return n%(s+p)==0 
        """
        :type n: int
        :rtype: bool
        """
        