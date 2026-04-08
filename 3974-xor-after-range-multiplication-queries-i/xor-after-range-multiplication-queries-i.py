class Solution(object):
    def xorAfterQueries(self, nums, queries):
        for [l,r,k,v] in queries:
            idx=l;
            while(idx<=r):
                nums[idx]=(nums[idx] * v) % (10**9 + 7)
                idx+=k
        res=nums[0];
        for i in nums[1:]:
            res^=i;
        return res
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        