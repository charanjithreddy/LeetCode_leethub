class Solution(object):
    def flowerGame(self, n, m):
        n_e=n//2;
        n_o=n-n_e;
        m_e=m//2;
        m_o=m-m_e;
        return n_e*m_o+n_o*m_e;


        """
        :type n: int
        :type m: int
        :rtype: int
        """
        