class Solution(object):
    def largestGoodInteger(self, num):
        a=0;
        b=1;
        c=2;
        res="";
        while(c<len(num)):
            if(num[a]==num[b]==num[c]):
                res=max(res,num[a]+num[b]+num[c]);
            a+=1;
            b+=1;
            c+=1;
        return res;
        """
        :type num: str
        :rtype: str
        """    