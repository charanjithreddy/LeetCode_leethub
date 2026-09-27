class Solution(object):
    def reverseParentheses(self, s):
        stack=[];
        for i in s:
            if(i==")"):
                t="";
                while(stack[-1]!="("):
                    t+=stack.pop(-1)[::-1];
                stack.pop(-1);
                stack.append(t);
            else:
                stack.append(i);
        return "".join(stack)
        """
        :type s: str
        :rtype: str
        """
        