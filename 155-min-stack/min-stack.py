class MinStack(object):

    def __init__(self):
        self.a=[];
        
    def push(self, val):
        self.a.append(val);
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.a.pop(len(self.a)-1);
        """
        :rtype: None
        """
        

    def top(self):
        return self.a[-1];
        """
        :rtype: int
        """
        

    def getMin(self):
        return min(self.a);
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()