class Solution(object):
    def maxFreqSum(self, s):
        d={};
        for i in s:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        vowels="aeiou";
        dv=set();
        dc=set();
        dv.add(0);
        dc.add(0);
        for i in d:
            if(i in vowels):
                dv.add(d[i]);
            else:
                dc.add(d[i]);
        return max(dc)+max(dv);       
        """
        :type s: str
        :rtype: int
        """