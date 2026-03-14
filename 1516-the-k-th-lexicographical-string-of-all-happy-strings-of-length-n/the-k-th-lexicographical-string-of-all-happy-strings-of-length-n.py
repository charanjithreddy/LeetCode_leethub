class Solution(object):
    def getHappyString(self, n, k):
        res=[];
        def func(s):
            if(len(s)==n):
                res.append(s);
                return;
            if(s[-1]=="a"):
                func(s+"b");
                func(s+"c");
            elif(s[-1]=="b"):
                func(s+"a");
                func(s+"c");
            else:
                func(s+"a");
                func(s+"b");
        func("a");
        func("b");
        func("c");
        if(len(res)<k):
            return ""
        return sorted(res)[k-1]
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        