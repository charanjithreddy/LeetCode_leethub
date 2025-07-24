class Solution(object):
    def myPow(self, x, n):
        def func(x,n):
            if n==0:
                return 1;
            if(x==0 or n==1):
                return x;
            if(n%2==0):
                temp=self.myPow(x,n//2);
                return temp*temp;
            else:
                temp=self.myPow(x,n//2);
                return x*temp*temp;
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
        