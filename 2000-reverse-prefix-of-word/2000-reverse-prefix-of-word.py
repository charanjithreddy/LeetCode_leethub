class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word;
        else:
            n=word.index(ch);
            o=word[0:n+1][::-1]+word[n+1:];
            return o;