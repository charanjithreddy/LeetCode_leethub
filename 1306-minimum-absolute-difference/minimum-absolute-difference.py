class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort();
        min_abs_diff=float('inf');
        for i in range(len(arr)-1):
            min_abs_diff=min(min_abs_diff,arr[i+1]-arr[i]);
        res=[];
        for i in range(len(arr)-1):
            if(arr[i+1]-arr[i]==min_abs_diff):
                res.append([arr[i],arr[i+1]]);
        return res;
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        