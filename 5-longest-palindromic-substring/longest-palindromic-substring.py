class Solution(object):
    def longestPalindrome(self, s):
        res=1;
        o=s[0];
        
        for i in range(len(s)-1):
            t=0;
            while(i-t>=0 and i+t<len(s)):
                if(s[i-t]==s[i+t]):
                    t+=1;
                else:
                    break;
            if(1+2*(t-1)>res):
                res=1+2*(t-1);
                o=s[i-t+1:i+t];
            if(s[i]==s[i+1]):
                t=0;
                while(i-t>=0 and i+t+1<len(s)):
                    if(s[i-t]==s[i+t+1]):
                        t+=1;
                    else:
                        break;
                if(2*t>res):
                    res=2*t;
                    o=s[i-t+1:i+t+1];
        return o;
        """
        :type s: str
        :rtype: str
        """
        