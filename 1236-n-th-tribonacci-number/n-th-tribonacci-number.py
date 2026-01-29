class Solution(object):
    def tribonacci(self, n):
        a=[0]*38;
        a[0]=0;
        a[1]=1;
        a[2]=1;
        t=2
        for i in range(3,len(a)):
            a[i]=a[i-1]+a[i-2]+a[i-3]
        return a[n];
        """
        :type n: int
        :rtype: int
        """
        