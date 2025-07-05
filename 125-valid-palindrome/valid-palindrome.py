class Solution(object):
    def isPalindrome(self, s):
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
        