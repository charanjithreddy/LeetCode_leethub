class Solution(object):
    def maxOperations(self, s):
        res=0;
        ones=0;
        flag=1;
        for i in s:
            if(i=='0'):
                if(flag==1):
                    res+=ones;
                flag=0;
            else:
                ones+=1;
                flag=1;
        return res;
        """
        :type s: str
        :rtype: int
        """