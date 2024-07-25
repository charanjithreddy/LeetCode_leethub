class Solution(object):
    def longestPalindrome(self, s):
        o="";
        for i in range(len(s)):
            for j in range(len(s),-1,-1):
                if(j-i>len(o)):
                    s1=s[i:j]
                    if(s1==s1[::-1] and len(s1)>len(o)):
                        o=s1;
        return o;
        """
        :type s: str
        :rtype: str
        """
        