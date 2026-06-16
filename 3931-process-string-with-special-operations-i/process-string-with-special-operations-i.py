class Solution(object):
    def processStr(self, s):
        res=[];
        for i in s:
            if(i=="*"):
                if(len(res)>0):
                    res=res[:-1];
            elif(i=="#"):
                res.extend(res);
            elif(i=="%"):
                res=res[::-1];
            else:
                res.append(i);
        return "".join(res)
        """
        :type s: str
        :rtype: str
        """
        