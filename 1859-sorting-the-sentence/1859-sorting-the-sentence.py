class Solution(object):
    def sortSentence(self, s):
        s=s.split();
        length=len(s);
        l=[""]*length;
        for i in range(length):
            l[int(s[i][-1])-1]=s[i][:-1];
        return ' '.join(l);        