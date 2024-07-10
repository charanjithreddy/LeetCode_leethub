class Solution(object):
    def reverse(self, x):
        sign=1;
        if(x<0):
            sign=-1;
            x=-x;
        
        s=str(x);
        x1=int(s[::-1]);
        if(x1>=-(2**31) and x1<=(2**31)-1):
            return sign*x1;
        else:
            return 0;
        """
        :type x: int
        :rtype: int
        """
        