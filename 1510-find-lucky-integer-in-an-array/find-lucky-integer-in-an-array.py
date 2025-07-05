class Solution(object):
    def findLucky(self, arr):
        o=-1;
        c=0;
        d={};
        for i in arr:
            if( i in d):
                d[i]+=1;
            else:
                d[i]=1;
        for i in d:
            if(d[i]>c and d[i]==i):
                o=i;
                c=d[i];
        return o;

        """
        :type arr: List[int]
        :rtype: int
        """
        