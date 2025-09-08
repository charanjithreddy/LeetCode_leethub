class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1,n+1):
            j=n-i;
            if(not(('0') in str(i)) and not('0' in str(j))):
                return [i,j]
        """
        :type n: int
        :rtype: List[int]
        """
        