class Solution(object):
    def lexicalOrder(self, n):
        l=sorted([str(i) for i in range(1,n+1)]);
        return [int(i) for i in l]
        """
        :type n: int
        :rtype: List[int]
        """
        