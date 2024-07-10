class Solution(object):
    def pivotInteger(self, n):
        for i in range(n+1):
            lsum=i*(i+1)/2;
            rsum=n*(n+1)/2-lsum+i;
            if(lsum==rsum):
                return i;
        return -1;        