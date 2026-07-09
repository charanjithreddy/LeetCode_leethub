class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        batch=[0 for _ in range(n)];
        grp_no=0;
        for i in range(1,len(nums)):
            if(nums[i]-nums[i-1]>maxDiff):
                grp_no+=1;
            batch[i]=grp_no;
        res=[];
        for u,v in queries:
            res.append(batch[u]==batch[v]);
        return res
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        