class Solution(object):
    def generateParenthesis(self, n):
        res=set();
        def func(open,close,s):
            if(open==close):
                if(open==n):
                    res.add(s);
                    return;
                else:
                    func(open+1,close,s+"(");
            if(open<n):
                func(open+1,close,s+"(");
            if(close<open):
                func(open,close+1,s+")")
        func(1,0,"(");
        return list(res);
        """
        :type n: int
        :rtype: List[str]
        """