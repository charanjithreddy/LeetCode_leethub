class Solution(object):
    def truncateSentence(self, s, k):
        s=s.split(" ");
        l=[];
        for i in range(k):
            l.append(s[i]);
        return " ".join(l);
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        