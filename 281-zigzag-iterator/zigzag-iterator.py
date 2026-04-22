class ZigzagIterator(object):

    def __init__(self, v1, v2):
        t=[];
        ind1=0;
        ind2=0;
        while(ind1<len(v1) and ind2<len(v2)):
            t.append(v1[ind1]);
            ind1+=1;
            t.append(v2[ind2]);
            ind2+=1;
        while(ind1<len(v1)):
            t.append(v1[ind1]);
            ind1+=1;
        while(ind2<len(v2)):
            t.append(v2[ind2]);
            ind2+=1;
        self.t=t;
        self.ind=0;
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        

    def next(self):
        self.ind+=1;
        return self.t[self.ind-1];
        """
        :rtype: int
        """
        

    def hasNext(self):
        return self.ind<len(self.t)
        """
        :rtype: bool
        """
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())