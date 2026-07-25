class Solution(object):
    def maxProduct(self, n):
        arr=[int(i) for i in str(n)]
        arr.sort();
        return arr[-1]*arr[-2]
        """
        :type n: int
        :rtype: int
        """
        