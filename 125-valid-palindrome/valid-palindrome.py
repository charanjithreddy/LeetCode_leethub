class Solution(object):
    def isPalindrome(self, s):
        left=0;
        right=len(s)-1;
        while(left<right):
            while(left<right and not(s[left].isalnum())):
                left+=1;
            while(right>left and not(s[right].isalnum())):
                right-=1;
            if(lower(s[left])!=lower(s[right])):
                return False;
            left+=1;
            right-=1;
        return True;
        """
        :type s: str
        :rtype: bool
        """