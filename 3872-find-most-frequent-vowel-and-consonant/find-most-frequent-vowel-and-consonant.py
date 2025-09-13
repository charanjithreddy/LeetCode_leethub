class Solution(object):
    def maxFreqSum(self, s):
        d={};
        for i in s:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        vowels="aeiou";
        dv={};
        dv['A']=0;
        dc={};
        dc['B']=0;
        for i in d:
            if(i in vowels):
                dv[i]=d[i];
            else:
                dc[i]=d[i];
        return max(list(dv.values()))+max(list(dc.values()));        
        """
        :type s: str
        :rtype: int
        """