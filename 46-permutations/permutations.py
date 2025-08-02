class Solution(object):
    def permute(self, nums):
        o=[];
        n=len(nums);
        def func(i,l):
            if(i==n):
                o.append(list(l));
                return;
            for j in range(len(l)+1):
                l.insert(j,nums[i])
                func(i+1,l);
                l.pop(j);           
        func(0,[]);
        return o;
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """