class MRUQueue(object):

    def __init__(self, n):
        self.a=[i for i in range(1,n+1)]
        """
        :type n: int
        """
        

    def fetch(self, k):
        t=self.a[k-1];
        for i in range(k-1,len(self.a)-1):
            self.a[i]=self.a[i+1]
        self.a[-1]=t;
        return t
        """
        :type k: int
        :rtype: int
        """
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)