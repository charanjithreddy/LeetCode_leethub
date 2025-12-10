class Solution(object):
    def countPermutations(self, complexity):
        if(complexity[0]!=sorted(complexity)[1] and min(complexity)==complexity[0]):
            res=1;
            for i in range(2,len(complexity)):
                res*=i;
                res%=(10**9+7);
            return res%(10**9+7);
        else:
            return 0;
        """
        :type complexity: List[int]
        :rtype: int
        """
        