class Solution(object):
    def replaceWords(self, dictionary, sentence):
        s=sentence.split();
        for i in dictionary:
            for j in range(len(s)):
                if(i==s[j][:len(i)]):
                    s[j]=i;
        return ' '.join(s);