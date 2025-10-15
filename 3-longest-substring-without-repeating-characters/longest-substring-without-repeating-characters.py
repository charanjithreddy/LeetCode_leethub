class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x=set();
        l=0;
        res=min(1,len(s));
        for i in range(len(s)):
            if(s[i] not in x):
                res=max(res,i-l+1);
                x.add(s[i]);
            else:
                res=max(res,i-l);
                while(s[l]!=s[i]):
                    x.remove(s[l]);
                    l+=1;
                x.remove(s[l]);
                l+=1;
                x.add(s[i])
        return res;


        """
        :type s: str
        :rtype: int
        """
        