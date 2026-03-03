class Solution(object):
    def findKthBit(self, n, k):
        def invert(s):
            temp=list(s);
            for i in range(len(temp)):
                if(temp[i]=="1"):
                    temp[i]="0";
                else:
                    temp[i]="1";
            return "".join(temp)
        def func(n):
            if(n==1):
                return "0";
            else:
                t=func(n-1);
                return t+"1"+invert(t)[::-1]
        return func(n)[k-1]
        """
        :type n: int
        :type k: int
        :rtype: str
        """