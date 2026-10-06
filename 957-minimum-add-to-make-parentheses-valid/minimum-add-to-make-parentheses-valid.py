class Solution(object):
    def minAddToMakeValid(self, s):
        stack=[];
        res=0;
        for i in s:
            if(i=="("):
                stack.append(i);
            elif(stack and stack[-1]=="("):
                stack.pop(-1);
            else:
                res+=1;
        return res+len(stack)

        """
        :type s: str
        :rtype: int
        """
        