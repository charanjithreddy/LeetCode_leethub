class Solution(object):
    def reverseParentheses(self, s):
        while "(" in s:
            start=0;
            end=0;
            for i in range(len(s)):
                if(s[i]=="("):
                    start=i;
                elif(s[i]==")"):
                    end=i;
                    break;
            s=s[:start]+s[start+1:end][::-1]+s[end+1:];
        return s
        """
        :type s: str
        :rtype: str
        """
        