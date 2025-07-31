class Solution(object):
    def findTheDifference(self, s, t):
        s1=sorted(s);
        t1=sorted(t);
        for i in range(len(s1)):
            if(s1[i]!=t1[i]):
                return t1[i];
        return t1[-1];
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        