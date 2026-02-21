class Solution(object):
    def countPrimeSetBits(self, left, right):
        def isprime(n):
            if(n<=1):
                return False
            i=2;
            while(i*i<=n):
                if(n%i==0):
                    return False;
                i+=1;
            return True
        res=0;
        for i in range(left,right+1):
            if(isprime(bin(i)[2:].count("1"))):
                res+=1;
        return res;
        """
        :type left: int
        :type right: int
        :rtype: int
        """