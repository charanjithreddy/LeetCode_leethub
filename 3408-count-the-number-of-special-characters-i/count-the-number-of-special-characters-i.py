class Solution(object):
    def numberOfSpecialChars(self, word):
        small=[0]*26;
        big=[0]*26;
        res=0;
        for i in word:
            if("a"<=i<="z"):
                if(big[ord(i)-ord('a')]==1 and small[ord(i)-ord('a')]==0):
                    res+=1;
                small[ord(i)-ord('a')]=1;
            else:
                if(small[ord(i)-ord('A')]==1 and big[ord(i)-ord('A')]==0):
                    res+=1;
                big[ord(i)-ord('A')]=1;
        return res;
        """
        :type word: str
        :rtype: int
        """
        