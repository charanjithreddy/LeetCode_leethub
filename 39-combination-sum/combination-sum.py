class Solution(object):
    def combinationSum(self, candidates, target):
        o=[];
        def func(i,s,l):
            if(i==len(candidates) or s>target):
                return;
            if(s==target):
                o.append(list(l));
                return;
            l.append(candidates[i]);
            func(i,s+candidates[i],l);
            l.pop();
            func(i+1,s,l)
        func(0,0,[]);
        return o;
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """