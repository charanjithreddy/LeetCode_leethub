class MyHashSet(object):

    def __init__(self):
        self.s=set();
        

    def add(self, key):
        self.s.add(key);
        """
        :type key: int
        :rtype: None
        """
        

    def remove(self, key):
        if(key in self.s):
            self.s.remove(key);
        """
        :type key: int
        :rtype: None
        """
        

    def contains(self, key):
        return key in self.s;
        """
        :type key: int
        :rtype: bool
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)