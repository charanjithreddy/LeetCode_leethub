class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        o=[];
        for i in range(len(nums)):
            if(nums[i]==key):
                o.append(i);
                x=max(0,i-k);
                for j in range(x,i):
                    o.append(j);
                x=min(len(nums)-1,i+k);
                for j in range(i+1,x+1):
                    o.append(j);
        return sorted(list(set(o)));
                

        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        