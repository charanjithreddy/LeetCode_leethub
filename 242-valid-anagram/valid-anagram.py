class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False;
        sh={i:s.count(i) for i in list(set(s))};
        th={i:t.count(i) for i in list(set(t))};
        if(len(sh)!=len(th)):
            return False;
        for i in sh:
            if(i not in th or sh[i]!=th[i]):
                return False;
        for i in th:
            if(i not in sh or sh[i]!=th[i]):
                return False;
        return True;
        """
        :type s: str
        :type t: str
        :rtype: bool
        """