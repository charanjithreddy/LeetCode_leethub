class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort();
        o=[];
        def func(i,l,s):
            if(s==target):
                o.append(list(l));
                return;
            if(i==len(candidates) or s>target):
                return;
            l.append(candidates[i]);
            func(i+1,l,s+candidates[i]);
            l.pop();
            j=i+1;
            while(j<len(candidates) and candidates[j]==candidates[i]):
                j+=1;
            func(j,l,s);
        func(0,[],0);
        return o;
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """