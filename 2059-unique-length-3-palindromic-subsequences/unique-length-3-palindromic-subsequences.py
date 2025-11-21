class Solution(object):
    def countPalindromicSubsequence(self, s):
        res=0;
        for i in set(s):
            res+=len(set(s[s.index(i)+1:len(s)-s[::-1].index(i)-1]));
        return res;
        """
        :type s: str
        :rtype: int
        """