class Solution(object):
    def checkOnesSegment(self, s):
        i=1;
        while(i<len(s) and s[i]==s[i-1]):
            i+=1;
        while(i<len(s)):
            if(s[i]=="1"):
                return False;
            i+=1
        return True
        """
        :type s: str
        :rtype: bool
        """