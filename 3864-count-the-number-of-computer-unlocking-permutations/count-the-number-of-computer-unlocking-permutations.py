class Solution(object):
    def countPermutations(self, complexity):
        def fact(n):
            if(n==0 or n==1):
                return 1;
            else:
                return (n*fact(n-1))%(10**9+7);
        if(complexity[0]!=sorted(complexity)[1] and min(complexity)==complexity[0]):
            return (fact(len(complexity)-1))%(10**9+7);
        else:
            return 0;
        """
        :type complexity: List[int]
        :rtype: int
        """
        