class Solution(object):
    def minOperations(self, s):
        res1=0;
        res2=0;
        s1=[int(i) for i in s];
        for i in range(len(s1)):
            if(s1[i]==i%2):
                res1+=1;
            if(s1[i]==(i+1)%2):
                res2+=1;
        return min(res1,res2)
        """
        :type s: str
        :rtype: int
        """
        