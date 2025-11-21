class Solution(object):
    def countPalindromicSubsequence(self, s):
        first={};
        last={};
        res=0;
        for i in set(s):
            first[i]=s.index(i);
            last[i]=len(s)-s[::-1].index(i)-1;
            res+=len(set(s[first[i]+1:last[i]]));
        return res;
        """
        :type s: str
        :rtype: int
        """