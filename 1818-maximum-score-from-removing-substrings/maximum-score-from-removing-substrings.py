class Solution(object):
    def maximumGain(self, s, x, y):
        stack=[];
        res=0;
        if(x>y):
            for i in range(len(s)):
                if(s[i]=="b" and len(stack)>0 and stack[-1]=="a"):
                    res+=x;
                    stack.pop();
                else:
                    stack.append(s[i]);
            s="".join(stack);
            stack=[];
            for i in range(len(s)):
                if(s[i]=="a" and len(stack)>0 and stack[-1]=="b"):
                    res+=y;
                    stack.pop();
                else:
                    stack.append(s[i]);
        else:
            for i in range(len(s)):
                if(s[i]=="a" and len(stack)>0 and stack[-1]=="b"):
                    res+=y;
                    stack.pop();
                else:
                    stack.append(s[i]);
            s="".join(stack);
            stack=[];
            for i in range(len(s)):
                if(s[i]=="b" and len(stack)>0 and stack[-1]=="a"):
                    res+=x;
                    stack.pop();
                else:
                    stack.append(s[i]);
        return res;      
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """