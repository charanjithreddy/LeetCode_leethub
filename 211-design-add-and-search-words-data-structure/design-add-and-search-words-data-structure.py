class Node():
    def __init__(self):
        self.next={};
        self.end=False;

class WordDictionary(object):
    def __init__(self):
        self.root=Node()

    def addWord(self, word):
        cur=self.root;
        for i in word:
            if(i not in cur.next):
                cur.next[i]=Node();
            cur=cur.next[i];
        cur.end=True;
        """
        :type word: str
        :rtype: None
        """

    def search(self, word):
        cur=self.root;
        def func(i,cur):
            if(i==len(word)):
                return cur.end
            if(word[i]=="."):
                for j in cur.next:
                    if(func(i+1,cur.next[j])):
                        return True;        
                return False;      
            elif(word[i] in cur.next):
                return func(i+1,cur.next[word[i]]);
            else:
                return False
        return func(0,cur);
        """
        :type word: str
        :rtype: bool
        """
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)