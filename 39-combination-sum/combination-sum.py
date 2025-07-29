class Solution(object):
    def combinationSum(self, candidates, target):
        o=[];
        def func(i,s,l):
            if(i==len(candidates) or s>target):
                return;
            if(s==target):
                o.append(list(l));
                return;
            for j in range(i,len(candidates)):
                l.append(candidates[j]);
                func(j,s+candidates[j],l);
                l.pop();
        func(0,0,[]);
        return o;
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """