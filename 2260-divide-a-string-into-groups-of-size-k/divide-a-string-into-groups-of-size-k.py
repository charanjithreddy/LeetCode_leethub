class Solution(object):
    def divideString(self, s, k, fill):
        o=[];
        t=0;
        for i in range(len(s)//k):
            o.append(s[k*i:k*i+k]);
            t=k*i+k;
        r=len(s)%k;
        if(r!=0):
            o.append(s[t:]+(k-r)*fill);
        return o
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        