class Solution(object):
    def minimumDistance(self, nums):
        res=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]==nums[j]==nums[k]):
                        if(res==-1):
                            res=abs(i-j)+abs(j-k)+abs(k-i)
                        else:
                            res=min(res,abs(i-j)+abs(j-k)+abs(k-i))
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        