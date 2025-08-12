class Solution(object):
    def getPermutation(self, n, k):
        k-=1;
        def fact(n):
            if(n==0 or n==1):
                return 1;
            else:
                return n*fact(n-1);
        s="";
        d=1;
        l=set();
        while(d<=n):
            x=fact(n-d);
            for i in range(1,n+1):
                if(i in l):
                    continue;
                if(k-x<0):
                    s+=str(i);
                    l.add(i);
                    break;
                k-=x;
            d+=1;
        return s;
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        