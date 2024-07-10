class Solution(object):
    def mostWordsFound(self, sentences):
        count=len(sentences[0].split());
        for i in range(1,len(sentences)):
            if(len(sentences[i].split())>count):
                count=len(sentences[i].split())
        return count;
        """
        :type sentences: List[str]
        :rtype: int
        """
        