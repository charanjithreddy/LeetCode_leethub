class Solution(object):
    def countBits(self, n):
        res=[0]*(n+1);
        ind=1;
        for i in range(1,n+1):
            if(ind*2==i):
                ind=i;
            res[i]=1+res[i-ind];
        return res
        """
        :type n: int
        :rtype: List[int]
        """
        