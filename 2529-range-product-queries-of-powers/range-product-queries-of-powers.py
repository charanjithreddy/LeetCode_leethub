class Solution(object):
    def productQueries(self, n, queries):
        t=[];
        n=bin(n)[2:][::-1];
        i=0;
        while(i<len(n)):
            if(n[i]=="1"):
                t.append(2**i);
            i+=1;

        o=[];
        for [a,b] in queries:
            temp=1;
            for x in range(a,b+1):
                temp*=t[x];
            o.append(temp%(10**9+7));
        return o;
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """