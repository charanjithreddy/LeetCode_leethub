class Solution(object):
    def minimumDeletions(self, s):
        n=len(s);
        a=[];
        b=[];
        b_cnt=0;
        for i in range(n):
            b.append(b_cnt);
            if(s[i]=="b"):
                b_cnt+=1;
        a_cnt=0;
        for i in range(n-1,-1,-1):
            a.append(a_cnt);
            if(s[i]=="a"):
                a_cnt+=1;
        a=a[::-1];
        return min([(a[i]+b[i]) for i in range(n)])
        """
        :type s: str
        :rtype: int
        """