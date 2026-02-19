class Solution(object):
    def countBinarySubstrings(self, s):
        res=0
        for i in range(len(s)-1):
            if(s[i]!=s[i+1]):
                cnt1=1;
                l=i;
                while(l>0 and s[l-1]==s[l]):
                    l-=1;
                    cnt1+=1;

                cnt2=1;
                r=i+1;
                while(r<len(s)-1 and s[r]==s[r+1]):
                    r+=1;
                    cnt2+=1;
                res+=min(cnt1,cnt2);


        
        return res;
        """
        :type s: str
        :rtype: int
        """
        