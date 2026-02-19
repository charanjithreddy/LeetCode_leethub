class Solution(object):
    def countBinarySubstrings(self, s):
        res=0
        prev=0;
        curr=1;
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                curr+=1;
            else:
                res+=min(curr,prev);
                prev=curr;
                curr=1;
        return res+min(prev,curr)
        
        """
        :type s: str
        :rtype: int
        """