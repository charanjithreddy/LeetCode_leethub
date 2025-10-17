class Trie(object):

    def __init__(self):
        self.l=[];
        

    def insert(self, word):
        self.l.append(word);
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        return word in self.l;
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        for i in self.l:
            if(i[:len(prefix)]==prefix):
                return True;
        return False;
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)