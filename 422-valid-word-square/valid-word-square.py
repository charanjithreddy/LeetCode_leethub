class Solution(object):
    def validWordSquare(self, words):
        try:
            for i in range(len(words)):
                for j in range(len(words[i])):
                    if(words[i][j]!=words[j][i]):
                        return False;
            return True;
        except IndexError as e:
            return False;
        """
        :type words: List[str]
        :rtype: bool
        """