class Solution(object):
    def divideString(self, s, k, fill):
        o=[];
        l=len(s);
        for i in range(l//k):
            o.append(s[k*i:k*(i+1)]);
        r=l%k;
        if(r!=0):
            o.append(s[k*((l//k-1)+1):]+(k-r)*fill);
        return o
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """