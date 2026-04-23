class Solution(object):
    def maxSameLengthRuns(self, s):
        t=[str(s[0])];
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                t[-1]+=s[i];
            else:
                t.append(str(s[i]));
        d={};
        for i in t:
            if(len(i) in d):
                d[len(i)]+=1;
            else:
                d[len(i)]=1;
        return max(d.values())
        """
        :type s: str
        :rtype: int
        """
        