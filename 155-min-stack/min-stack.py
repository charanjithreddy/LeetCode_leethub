class MinStack(object):

    def __init__(self):
        self.a=[];
        
    def push(self, val):
        if(len(self.a)==0):
            self.a.append([val,val]);
        else:
            self.a.append([val,min(val,self.a[-1][1])]);
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
        return self.a[-1][0];
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.a[-1][1];
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()