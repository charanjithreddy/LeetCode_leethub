class Solution(object):
    def longestSubsequence(self, s, k):
        l=len(s);
        v=0;
        o=0;
        s=[int(i) for i in s];
        for i in range(l-1,-1,-1):
            if(v+(s[i])*(2**(l-i-1))<=k):
                v+=(s[i])*(2**(l-i-1));
                o+=1;
            elif(s[i]==0):
                o+=1;
        return o;
            

        """
        :type s: str
        :type k: int
        :rtype: int
        """
        