class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        t=[];
        ones=0;
        for i in s:
            if(i=="1"):
                ones+=1;
            if(not t):
                t.append(i);
            else:
                if(i in t[-1]):
                    t[-1]+=i;
                else:
                    t.append(i);
        res=0;
        for i in range(1, len(t)-1):
            if("1" in t[i] and "0" in t[i-1] and "0" in t[i+1]):
                res=max(res,len(t[i-1])+len(t[i+1]));
        return ones+res

        """
        :type s: str
        :rtype: int
        """
        