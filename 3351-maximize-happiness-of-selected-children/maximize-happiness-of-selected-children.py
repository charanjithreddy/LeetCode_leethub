class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        res=0;
        for i in range(min(k,len(happiness))):
            res+=max(happiness[i]-i,0);
        return res;
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """