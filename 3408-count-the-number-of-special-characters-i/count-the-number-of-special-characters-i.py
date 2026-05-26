class Solution(object):
    def numberOfSpecialChars(self, word):
        small=[0]*26;
        big=[0]*26;
        for i in word:
            if("a"<=i<="z"):
                small[ord(i)-ord('a')]=1;
            else:
                big[ord(i)-ord('A')]=1;
        res=0;
        for i in range(26):
            if(small[i]==1 and big[i]==1):
                res+=1;
        return res
        """
        :type word: str
        :rtype: int
        """
        