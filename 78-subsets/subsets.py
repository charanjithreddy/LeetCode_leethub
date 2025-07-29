class Solution(object):
    def subsets(self, nums):
        o=[];
        def func(i,l):
            if(i==len(nums)):
                o.append(list(l));
                return;
            func(i+1,list(l));
            l.append(nums[i]);
            func(i+1,list(l));
        func(0,[]);
        return o;
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        