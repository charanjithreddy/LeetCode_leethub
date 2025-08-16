class Solution(object):
    def maximum69Number (self, num):
        num=str(num);
        ind=-1;
        for i in range(len(num)):
            if(num[i]=="6"):
                ind=i;
                break;
        if(ind==-1):
            return int(num);
        else:
            return int(num)+3*(10**(len(str(num))-i-1));
        """
        :type num: int
        :rtype: int
        """
        