class Solution(object):
    def gcdOfOddEvenSums(self, n):
        a=0;
        b=0;
        for i in range(1,2*n+1):
            if(i%2==0):
                a+=i;
            else:
                b+=i;
        while(b):
            a,b=b,a%b
        return a
        """
        :type n: int
        :rtype: int
        """
        