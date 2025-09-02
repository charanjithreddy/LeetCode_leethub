class Solution(object):
    def minCostClimbingStairs(self, cost):
        a=[0]*(len(cost)+1);
        for i in range(2,len(a)):
            a[i]=min(a[i-1]+cost[i-1],a[i-2]+cost[i-2]);
        return a[-1];

        """
        :type cost: List[int]
        :rtype: int
        """
        