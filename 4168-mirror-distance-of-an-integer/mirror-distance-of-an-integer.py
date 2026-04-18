class Solution(object):
    def mirrorDistance(self, n):
        return abs(n-int(str(n)[::-1]))
        """
        :type n: int
        :rtype: int
        """