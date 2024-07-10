class Solution(object):
    def isStrictlyPalindromic(self, n):
        for i in range(2,n-1):
            s=[];
            t=n;
            while(t>0):
                s.append(str(t%i));
                t=t/i;
                a=''.join(s);
            if(s[0]!=s[len(s)-1] and a!=a[::-1]):
                return False;
        return True;
        """
        :type n: int
        :rtype: bool
        """
        