class Solution(object):
    def findLexSmallestString(self, s, a, b):
        l=set();
        def func(s):
            if(s in l):
                return;
            l.add(s);
            func(s[-1*b:]+s[:-1*b]);
            s=list(s);
            for i in range(1,len(s),2):
                s[i]=str((int(s[i])+a)%10);
            s="".join(s);
            func(s);

            
        func(s);
        return min(l);
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        