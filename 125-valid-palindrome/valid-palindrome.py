class Solution(object):
    def isPalindrome(self, s):
        s=list(s);
        s=''.join([lower(i) for i in s if i.isalnum()]);
        return s==s[::-1];
        s1="";
        for i in s:
            if(i.isalnum()):
                s1+=i;
        s1=lower(s1);
        return s1==s1[::-1];
        """
        :type s: str
        :rtype: bool
        """