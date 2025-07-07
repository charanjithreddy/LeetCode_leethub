class Solution(object):
    def evalRPN(self, tokens):
        o=[];
        for i in tokens:
            if(i=="+"):
                res=int(o.pop())+int(o.pop());
                o.append(res);
            elif(i=="-"):
                res=int(o.pop());
                
                o.append(int(o.pop())-res);
            elif(i=="*"):
                res=int(o.pop())*int(o.pop());
                o.append(res);
            elif(i=="/"):
                res=float(o.pop());
                res=int(o.pop())/res;
                o.append(int(res));
            else:
                o.append(int(i));
        return o[0];
        """
        :type tokens: List[str]
        :rtype: int
        """