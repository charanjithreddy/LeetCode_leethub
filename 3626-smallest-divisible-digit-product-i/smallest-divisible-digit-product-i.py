class Solution(object):
    def smallestNumber(self, n, t):
        for i in range(n,n+10):
            temp=i;
            prod=1;
            while(temp>0):
                prod*=temp%10;
                temp//=10;
            if(prod%t==0):
                return i;
        
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        