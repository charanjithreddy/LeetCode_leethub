class Solution(object):
    def canAliceWin(self, n):
        cnt=0;
        ind=10;
        while(n>=ind):
            n-=ind;
            cnt+=1;
            ind-=1;
        return cnt%2!=0
        """
        :type n: int
        :rtype: bool
        """
        