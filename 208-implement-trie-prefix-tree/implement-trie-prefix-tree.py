class Node():
    def __init__(self):
        self.next={};
        self.last=False;

class Trie(object):

    def __init__(self):
        self.root=Node();
        

    def insert(self, word):
        temp=self.root;
        for i in word:
            if(i not in temp.next):
                temp.next[i]=Node();
            temp=temp.next[i];
        temp.last=True;
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        temp=self.root;
        for i in word:
            if(i not in temp.next):
                return False;
            temp=temp.next[i];
        return temp.last;
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        temp=self.root;
        for i in prefix:
            if(i not in temp.next):
                return False;
            temp=temp.next[i];
        return True;
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)