class Solution(object):
    def isValid(self, s):
        stack=[];
        l=0;
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i);
                l+=1;
            else:
                if(i==')' and l>0 and stack[l-1]=='('):
                    stack.pop(l-1);
                    l-=1;
                elif(i==']' and l>0  and stack[l-1]=='['):
                    stack.pop(l-1);
                    l-=1;
                elif(i=='}' and l>0  and stack[l-1]=='{'):
                    stack.pop(l-1);
                    l-=1;
                else:
                    return False;
        return len(stack)==0;
        """
        :type s: str
        :rtype: bool
        """