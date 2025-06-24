class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        o=set();
        for i in range(len(nums)):
            if(nums[i]==key):
                o.add(i);
                x=max(0,i-k);
                for j in range(x,i):
                    o.add(j);
                x=min(len(nums)-1,i+k);
                for j in range(i+1,x+1):
                    o.add(j);
        return sorted(list(o));
                

        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        