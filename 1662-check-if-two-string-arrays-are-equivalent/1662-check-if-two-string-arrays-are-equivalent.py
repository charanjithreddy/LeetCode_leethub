class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        if(word1[0][0]==word2[0][0]):
            for i in range(1,len(word1)):
                word1[0]+=word1[i];
            for i in range(1,len(word2)):
                word2[0]+=word2[i];
            if(word1[0]==word2[0]):
                return True;
            else:
                return False;
        else:
            return False;
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        