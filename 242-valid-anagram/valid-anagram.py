class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False;
        for i in list(set(t)):
            if(i not in s):
                return False;
            elif(t.count(i)!=s.count(i)):
                return False;
        return True;        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """