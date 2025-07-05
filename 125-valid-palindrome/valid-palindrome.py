class Solution(object):
    def isPalindrome(self, s):
        s=''.join([lower(i) for i in list(s) if i.isalnum()]);
        return s==s[::-1];
        """
        :type s: str
        :rtype: bool
        """