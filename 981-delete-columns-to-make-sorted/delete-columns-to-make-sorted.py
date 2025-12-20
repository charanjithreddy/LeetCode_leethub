class Solution(object):
    def minDeletionSize(self, strs):
        l=max([len(i) for i in strs])
        a=[[] for i in range(l)];
        for i in strs:
            for j in range(len(i)):
                a[j].append(i[j]);
        res=0;
        for i in a:
            if(sorted(i)!=i):
                res+=1;
        return res;
        """
        :type strs: List[str]
        :rtype: int
        """
        