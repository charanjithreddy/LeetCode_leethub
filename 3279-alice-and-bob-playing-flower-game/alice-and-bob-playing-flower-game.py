class Solution(object):
    def flowerGame(self, n, m):
        return (n//2)*(m-(m//2))+(n-(n//2))*(m//2);
        """
        :type n: int
        :type m: int
        :rtype: int
        """