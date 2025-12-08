class Solution(object):
    def countTriples(self, n):
        res=0;
        for a in range(1,n):
            for b in range(a+1,n):
                c=math.sqrt(a*a+b*b);
                if(c==int(c) and c<=n):
                    if(a==b):
                        res+=1;
                    else:
                        res+=2;
        return res;
        """
        :type n: int
        :rtype: int
        """