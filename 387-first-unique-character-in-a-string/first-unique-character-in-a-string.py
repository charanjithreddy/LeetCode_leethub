class Solution(object):
    def firstUniqChar(self, s):
        d={};
        for i in range(len(s)):
            if(s[i] in d):
                d[s[i]].append(i);
            else:
                d[s[i]]=[i];
        for i in s:
            if(len(d[i])==1):
                return d[i][0];
        return -1;

        """
        :type s: str
        :rtype: int
        """
        