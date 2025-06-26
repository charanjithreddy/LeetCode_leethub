class Solution(object):
    def longestSubsequence(self, s, k):
        l=len(s);
        v=0;
        o=0;
        for i in range(len(s)-1,-1,-1):
            if(v+int(s[i])*(2**(l-i-1))<=k):
                v+=int(s[i])*(2**(l-i-1));
                o+=1;
            elif(s[i]=="0"):
                o+=1;
        return o;
            

        """
        :type s: str
        :type k: int
        :rtype: int
        """
        