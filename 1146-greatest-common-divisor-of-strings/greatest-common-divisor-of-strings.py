class Solution(object):
    def gcdOfStrings(self, str1, str2):
        res="";
        if(len(str2)<len(str1)):
            for i in range(1,len(str2)+1):
                t1=str1.split(str2[:i])
                t2=str2.split(str2[:i])
                if("".join(t1)=="" and "".join(t2)==""):
                    res=max(res,str2[:i]);
            
        else:
            for i in range(1,len(str1)+1):
                t1=str1.split(str1[:i]);
                t2=str2.split(str1[:i]);
                if("".join(t1)=="" and "".join(t2)==""):
                    res=max(res,str1[:i]);
        return res;

        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        