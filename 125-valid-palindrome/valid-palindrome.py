class Solution(object):
    def isPalindrome(self, s):
        s=''.join([lower(i) for i in list(s) if i.isalnum()]);
        l=len(s);
        for i in range(l//2):
            if(s[i]!=s[l-i-1]):
                return False;
        return True;
        """
        :type s: str
        :rtype: bool
        """