class Solution(object):
    def productQueries(self, n, queries):
        t=[];
        while(n>0):
            t.insert(0,(2**(int(math.log(n,2)))));
            n-=2**(int(math.log(n,2)));
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