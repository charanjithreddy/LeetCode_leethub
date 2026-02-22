class Solution(object):
    def binaryGap(self, n):
        res=0;
        b=bin(n)[2:];
        ind=-1;
        for i in range(len(b)):
            if(b[i]=="1"):
                if(ind!=-1):
                    res=max(res,i-ind)
                ind=i;
                
        return res;

        """
        :type n: int
        :rtype: int
        """
        