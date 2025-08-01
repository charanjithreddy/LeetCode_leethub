class Solution(object):
    def generateParenthesis(self, n):
        o=[];
        def func(s,open,close):
            if(open>n or close>n):
                return;
            if(open==n and close==n):
                o.append(str(s));
                return;
            if(open==n):
                func(s+")",open,close+1);
            if(open==0 or open==close):
                func(s+"(",open+1,close);
            if(open>close):
                func(s+"(",open+1,close);
                func(s+")",open,close+1);
        func("",0,0);
        return list(set(o));
        """
        :type n: int
        :rtype: List[str]
        """