class Solution(object):
    def minOperations(self, s):
        res1=0;
        res2=0;
        for i in range(len(s)):
            if(s[i]==str(i%2)):
                res1+=1;
            if(s[i]==str((i+1)%2)):
                res2+=1;
        return min(res1,res2)
        """
        :type s: str
        :rtype: int
        """