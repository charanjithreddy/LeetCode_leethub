class Solution(object):
    def maxFreqSum(self, s):
        d={};
        for i in s:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        dv=0;
        dc=0;
        for i in d:
            if(i in "aeiou"):
                dv=max(dv,d[i]);
            else:
                dc=max(dc,d[i]);
        return dv+dc;      
        """
        :type s: str
        :rtype: int
        """