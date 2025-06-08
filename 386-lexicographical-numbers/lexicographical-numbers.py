class Solution(object):
    def lexicalOrder(self, n):
        return [int(i) for i in sorted([str(i) for i in range(1,n+1)])]
        """
        :type n: int
        :rtype: List[int]
        """
        