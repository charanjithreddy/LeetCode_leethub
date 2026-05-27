class Solution(object):
    def numberOfSpecialChars(self, word):
        lower=[-1]*26;
        upper=[-1]*26;
        for i in range(len(word)):
            if('a'<=word[i]<='z'):
                lower[ord(word[i])-ord('a')]=i;
            else:
                if(upper[ord(word[i])-ord('A')]==-1):
                    upper[ord(word[i])-ord('A')]=i;
        res=0;
        for i in range(26):
            if(upper[i]!=-1 and lower[i]!=-1 and lower[i]<upper[i]):
                res+=1;
        return res
            
        """
        :type word: str
        :rtype: int
        """
        