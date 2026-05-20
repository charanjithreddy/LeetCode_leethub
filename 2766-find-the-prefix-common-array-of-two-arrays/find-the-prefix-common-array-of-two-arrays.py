class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        d={}
        n=len(A);
        for i in range(1,n+1):
            d[i]=0;
        C=[];
        cnt=0;
        for i in range(n):
            d[A[i]]+=1;
            d[B[i]]+=1;
            C.append(list(d.values()).count(2));
        return C
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """