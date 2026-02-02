class HitCounter(object):

    def __init__(self):
        self.a=[];
        

    def hit(self, timestamp):
        self.a.append(timestamp);
        """
        :type timestamp: int
        :rtype: None
        """
        

    def getHits(self, timestamp):
        res=0;
        for i in self.a:
            if(timestamp-300<i<=timestamp):
                res+=1;
        return res;
        """
        :type timestamp: int
        :rtype: int
        """
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)