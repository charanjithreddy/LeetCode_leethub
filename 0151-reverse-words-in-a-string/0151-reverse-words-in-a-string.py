class Solution(object):
    def reverseWords(self, s):
        s=[x.strip() for x in s.split()];
        s[:]=s[::-1];
        return " ".join(s);

        """
        :type s: str
        :rtype: str
        """
        