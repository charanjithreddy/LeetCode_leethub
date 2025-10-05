class Solution(object):
    def reverse(self, x):
        mul=1;
        if(x<0):
            mul=-1;
            x*=-1;
        res=int(str(x)[::-1]);
        res*=mul;
        if(-1*2**31<=res<=2**31-1):
            return res;
        else:
            return 0;
        """
        :type x: int
        :rtype: int
        """