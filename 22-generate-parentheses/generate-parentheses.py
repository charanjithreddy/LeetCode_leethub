class Solution(object):
    def generateParenthesis(self, n):
        res=[];
        def func(open,close,s):
            if(open==close):
                if(open==n):
                    if(s not in res):
                        res.append(s);
                    return;
                else:
                    func(open+1,close,s+"(");
            if(open<n):
                func(open+1,close,s+"(");
            if(close<open):
                func(open,close+1,s+")")


        func(1,0,"(");
        return res;
        """
        :type n: int
        :rtype: List[str]
        """