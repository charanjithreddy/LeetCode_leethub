class Solution(object):
    def isPalindrome(self, x):
        s=str(x);
        s1=s[::-1];
        if(s==s1):
            return True;
        else:
            return False;
        """
        :type x: int
        :rtype: bool
        """
        