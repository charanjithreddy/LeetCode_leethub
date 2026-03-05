class Solution(object):
    def minOperations(self, s):
        res1=0;
        res2=0;
        s1=list(s);
        s2=list(s);
        for i in range(len(s1)):
            if(int(s[i])==i%2):
                res1+=1;
            if(int(s[i])==(i+1)%2):
                res2+=1;
        return min(res1,res2)
        """
        :type s: str
        :rtype: int
        """
        