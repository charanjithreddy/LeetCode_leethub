class Solution(object):
    def subtractProductAndSum(self, n):
        p=1;
        s=0;
        while(n!=0):
            p*=(n%10);
            s+=n%10;
            n/=10;
        return p-s;

        """
        :type n: int
        :rtype: int
        """
        