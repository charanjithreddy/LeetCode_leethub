class Solution(object):
    def maxFreqSum(self, s):
        vowels="aeiou";
        dv={};
        dv['A']=0;
        dc={};
        dc['B']=0;
        for i in s:
            if(i in vowels):
                if(i in dv):
                    dv[i]+=1;
                else:
                    dv[i]=1;
            else:
                if(i in dc):
                    dc[i]+=1;
                else:
                    dc[i]=1;
        return max(list(dv.values()))+max(list(dc.values()));
        """
        :type s: str
        :rtype: int
        """
        