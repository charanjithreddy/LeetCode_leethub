class Solution(object):
    def largestGoodInteger(self, num):
        res="";
        for i in range(2,len(num)):
            if(num[i-2]==num[i-1]==num[i]):
                res=max(res,num[i-2:i+1]);
        return res;
        """
        :type num: str
        :rtype: str
        """