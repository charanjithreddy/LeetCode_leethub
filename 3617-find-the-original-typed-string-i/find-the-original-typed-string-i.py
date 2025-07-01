class Solution(object):
    def possibleStringCount(self, word):
        o=1;
        curr=word[0];
        t=0;
        for i in word:
            if(i==curr):
                t+=1;
            else:
                o+=(t-1);
                t=1;
                curr=i;
        o+=t-1;
        return o;
        """
        :type word: str
        :rtype: int
        """