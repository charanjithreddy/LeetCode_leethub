class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False;
        sh={};
        th={};
        for i in s:
            if(i not in sh):
                sh[i]=1;
            else:
                sh[i]+=1;
        for i in t:
            if(i not in th):
                th[i]=1;
            else:
                th[i]+=1;
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