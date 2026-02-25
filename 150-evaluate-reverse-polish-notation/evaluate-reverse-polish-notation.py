class Solution(object):
    def evalRPN(self, tokens):
        stack=[];
        for i in tokens:
            if(i=="+"):
                b=stack.pop();
                a=stack.pop();
                stack.append(int(a)+int(b));
            elif(i=="-"):
                b=stack.pop();
                a=stack.pop();
                stack.append(int(a)-int(b))
            elif(i=="*"):
                b=stack.pop();
                a=stack.pop();
                stack.append(int(a)*int(b));
            elif(i=="/"):
                b=stack.pop();
                a=stack.pop();
                stack.append(int(a)/float(b));
            else:
                stack.append(i);
        return int(stack[0]);

        """
        :type tokens: List[str]
        :rtype: int
        """
        