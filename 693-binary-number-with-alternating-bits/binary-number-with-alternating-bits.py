class Solution(object):
    def hasAlternatingBits(self, n):
        temp=n%2;
        n//=2;
        while(n>0):
            if(n%2==temp):
                return False;
            temp=n%2;
            n//=2;
        return True;
        """
        :type n: int
        :rtype: bool
        """
        