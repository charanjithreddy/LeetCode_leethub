class Solution(object):
    def makeFancyString(self, s):
        if(len(s)<3):
            return s;
        o=[];
        for i in range(len(s)-2):
            if(s[i]==s[i+1]==s[i+2]):
                continue;
            o.append(s[i]);
        o.append(s[-2]);
        o.append(s[-1]);
        return ''.join(o);
        """
        :type s: str
        :rtype: str
        """