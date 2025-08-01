class Solution(object):
    def generateParenthesis(self, n):
        o=[];
        def func(s,open,close):
            if(open==close):
                if(open==n):
                    o.append(s);
                else:
                    func(s+"(",open+1,close);
            if(open>close):
                if(open==n):
                    func(s+")",open,close+1);
                else:
                    func(s+"(",open+1,close);
                    func(s+")",open,close+1);
        func("",0,0);
        return list(set(o));
        """
        :type n: int
        :rtype: List[str]
        """