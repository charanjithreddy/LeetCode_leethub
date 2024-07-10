class Solution(object):
    def findPermutationDifference(self, s, t):
        o=0;
        for i in range(len(s)):
            o+=abs(i-t.index(s[i]));
        return o;