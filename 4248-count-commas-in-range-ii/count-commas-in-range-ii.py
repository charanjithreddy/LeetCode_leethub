class Solution(object):
    def countCommas(self, n):
        res=0;
        if(n>=10**3):
            if(n>=10**6):
                res+=10**6-1000
            else:
                res+=n-1000+1;
        if(n>=10**6):
            if(n>=10**9):
                res+=2*(10**9-10**6);
            else:
                res+=2*(n-10**6+1);
        if(n>=10**9):
            if(n>=10**12):
                res+=3*(10**12-10**9);
            else:
                res+=3*(n-10**9+1);
        if(n>=10**12):
            if(n>=10**15):
                res+=4*(10**15-10**12);
            else:
                res+=4*(n-10**12+1);
        if(n>=10**15):
            res+=5
        return res

        
        return res
        """
        :type n: int
        :rtype: int
        """
        