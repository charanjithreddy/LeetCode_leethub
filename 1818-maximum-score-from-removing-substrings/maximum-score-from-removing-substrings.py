class Solution(object):
    def maximumGain(self, s, x, y):
        stack=[];
        res=0;
        def func(s,check,value):
            res=0;
            for i in range(len(s)):
                if(s[i]==check[1] and len(stack)>0 and stack[-1]==check[0]):
                    res+=value;
                    stack.pop();
                else:
                    stack.append(s[i]);
            return res;
        if(x>y):
            res+=func(s,"ab",x)
            s="".join(stack);
            stack=[];
            res+=func(s,"ba",y)
        else:
            res+=func(s,"ba",y);
            s="".join(stack);
            stack=[];
            res+=func(s,"ab",x);
        return res;      
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """