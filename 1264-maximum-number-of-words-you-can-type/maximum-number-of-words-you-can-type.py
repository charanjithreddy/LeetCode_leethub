class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        res=0;
        text=text.split();
        for i in text:
            for j in brokenLetters:
                if(j in i):
                    res+=1;
                    break;
        return len(text)-res;
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        