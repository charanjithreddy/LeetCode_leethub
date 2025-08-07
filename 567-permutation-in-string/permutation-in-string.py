class Solution(object):
    def checkInclusion(self, s1, s2):
        if(len(s1)>len(s2)):
            return False;
        a=[0]*26;
        for i in s1:
            a[ord(i)-ord('a')]+=1;
        a=''.join([str(i) for i in a]);
        t=[0]*26;
        for i in range(len(s1)):
            t[ord(s2[i])-ord('a')]+=1;
        i=0;
        j=len(s1)-1;
        while(j<len(s2)):
            if(a==''.join([str(x) for x in t])):
                return True;
            t[ord(s2[i])-ord('a')]-=1;
            i+=1;
            j+=1;
            if(j<len(s2)):
                t[ord(s2[j])-ord('a')]+=1;
        return False;
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """