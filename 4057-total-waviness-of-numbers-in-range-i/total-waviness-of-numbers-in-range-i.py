class Solution(object):
    def totalWaviness(self, num1, num2):
        res=0;
        for i in range(num1,num2+1):
            s=str(i);
            for j in range(1,len(s)-1):
                if(s[j]>s[j+1] and s[j]>s[j-1]) or (s[j]<s[j+1] and s[j]<s[j-1]):
                    res+=1;
        return res
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        