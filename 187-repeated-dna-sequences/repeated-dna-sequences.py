class Solution(object):
    def findRepeatedDnaSequences(self, s):
        d={}
        for i in range(len(s)-10+1):
            t=s[i:i+10];
            if(t in d):
                d[t]+=1;
            else:
                d[t]=1;
        return [i for i in d if d[i]>1]
        """
        :type s: str
        :rtype: List[str]
        """
        