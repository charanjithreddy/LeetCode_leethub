class Solution(object):
    def myPow(self, x, n):
        def func(x,n):
            if n==0:
                return 1;
            if(x==0 or n==1):
                return x;
            if(n%2==0):
                return self.myPow(x*x,n//2);
            else:
                return x*self.myPow(x*x,n//2);
        res=func(x,abs(n));
        if(n>=0):
            return res;
        else:
            return 1.0/res;
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        