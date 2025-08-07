class Solution(object):
    def checkInclusion(self, s1, s2):
        i=0;
        j=len(s1);
        s=sorted(list(s1));
        while(j<=len(s2)):
            x=list(s2[i:j]);
            if(sorted(x)==s):
                return True;
            i+=1;
            j+=1;
        return False;
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """