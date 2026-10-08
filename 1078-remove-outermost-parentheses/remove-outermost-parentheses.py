class Solution(object):
    def removeOuterParentheses(self, s):
        res="";
        o=0;
        c=0;
        temp="";
        for i in s:
            if(i=="("):
                o+=1;
            else:
                c+=1;
            temp+=i;
            if(o==c):
                res+=temp[1:-1];
                temp="";
                o=0;
                c=0;
        return res
        """
        :type s: str
        :rtype: str
        """
        