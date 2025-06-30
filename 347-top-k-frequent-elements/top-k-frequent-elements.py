class Solution(object):
    def topKFrequent(self, nums, k):
        d={};
        for i in nums:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        c={i:[] for i in range(len(nums)+1)};
        for i in d:
            c[d[i]].append(i);
        o=[];
        for i in c:
            o.extend(c[i]);
        return o[-1*k:];

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        