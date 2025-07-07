class Solution(object):
    def evalRPN(self, tokens):
        o=[];
        for i in tokens:
            if(i=="+"):
                o.append(int(o.pop())+int(o.pop()));
            elif(i=="-"):
                res=int(o.pop());
                o.append(int(o.pop())-res);
            elif(i=="*"):
                o.append(int(o.pop())*int(o.pop()));
            elif(i=="/"):
                res=float(o.pop());
                o.append(int(int(o.pop())/res));
            else:
                o.append(int(i));
        return o[0];
        """
        :type tokens: List[str]
        :rtype: int
        """