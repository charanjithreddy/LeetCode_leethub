class Solution(object):
    def sumZero(self, n):
        if(n%2==0):
            l=[];
            for i in range(1,n/2+1):
                l.extend([i,-1*i]);
            return l;
        else:
            l=[];
            l.append(0);
            for i in range(1,n/2+1):
                l.extend([i,-1*i]);
            return l;