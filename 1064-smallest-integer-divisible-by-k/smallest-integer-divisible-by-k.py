class Solution(object):
    def smallestRepunitDivByK(self, k):
        s=set();
        start=1;
        l=1;
        while(start not in s):
            s.add(start);
            if(start%k==0):
                return l
            start=(start*10+1)%k;
            l+=1;
        return -1;
        """
        :type k: int
        :rtype: int
        """