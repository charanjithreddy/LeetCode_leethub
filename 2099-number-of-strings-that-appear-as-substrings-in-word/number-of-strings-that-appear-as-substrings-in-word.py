class Solution(object):
    def numOfStrings(self, patterns, word):
        res=0;
        for i in patterns:
            if(i in word):
                res+=1;
        return res
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        