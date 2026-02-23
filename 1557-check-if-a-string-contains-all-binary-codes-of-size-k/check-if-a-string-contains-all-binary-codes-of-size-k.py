class Solution(object):
    def hasAllCodes(self, s, k):
        t=set();
        for i in range(len(s)-k+1):
            t.add(s[i:i+k]);
        return len(t)==2**k

        """
        :type s: str
        :type k: int
        :rtype: bool
        """