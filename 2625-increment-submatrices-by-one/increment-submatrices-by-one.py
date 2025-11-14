class Solution(object):
    def rangeAddQueries(self, n, queries):
        a=[[0 for i in range(n)] for i in range(n)];
        for i in queries:
            for j in range(i[0],i[2]+1):
                a[j][i[1]]+=1;
                if(i[3]+1<n):
                    a[j][i[3]+1]-=1;
        for i in range(n):
            for j in range(1,n):
                a[i][j]+=a[i][j-1];
        return a;
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """