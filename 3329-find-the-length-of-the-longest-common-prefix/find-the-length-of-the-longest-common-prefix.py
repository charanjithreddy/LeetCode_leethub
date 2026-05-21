class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        s=set();
        res=0;
        for i in arr1:
            t=""
            for j in str(i):
                t+=j;
                s.add(t);
        for i in arr2:
            t="";
            for j in str(i):
                t+=j;
                if(t in s):
                    res=max(res,len(t));
        return res
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        