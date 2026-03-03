class Solution(object):
    def findKthBit(self, n, k):
        def func(n):
            if(n==1):
                return "0";
            else:
                t=func(n-1);
                invert="";
                for i in t:
                    if(i=="1"):
                        invert+="0";
                    else:
                        invert+="1";
                return t+"1"+invert[::-1]
        return func(n)[k-1]
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        