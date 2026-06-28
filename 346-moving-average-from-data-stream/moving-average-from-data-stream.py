class MovingAverage(object):

    def __init__(self, size):
        self.arr=[];
        self.size=size*1.0;
        """
        :type size: int
        """
        

    def next(self, val):
        if(len(self.arr)<self.size):
            self.arr.append(val);
            return (sum(self.arr)*1.0)/len(self.arr);
        else:
            self.arr.pop(0);
            self.arr.append(val);
            return (sum(self.arr)*1.0)/len(self.arr)
        """
        :type val: int
        :rtype: float
        """
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)