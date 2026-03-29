class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        self.s=set();
        for i in range(maxNumbers):
            self.s.add(i);
        """
        :type maxNumbers: int
        """
        

    def get(self):
        for i in self.s:
            t=i;
            self.s.remove(t);
            return t
        return -1
        """
        :rtype: int
        """
        

    def check(self, number):
        return number in self.s
        """
        :type number: int
        :rtype: bool
        """
        

    def release(self, number):
        self.s.add(number)
        """
        :type number: int
        :rtype: None
        """
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)