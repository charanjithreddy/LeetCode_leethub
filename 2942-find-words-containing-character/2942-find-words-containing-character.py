class Solution(object):
    def findWordsContaining(self, words, x):
        o=[];
        for i in range(len(words)):
            if (x in words[i]):
                o.append(i);
        return o;
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        