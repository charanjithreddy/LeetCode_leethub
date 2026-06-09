class Solution(object):
    def maxTotalValue(self, nums, k):
        maxi=float("-inf");
        mini=float("inf");
        for i in nums:
            maxi=max(maxi,i);
            mini=min(mini,i)
        return k*(maxi-mini)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        