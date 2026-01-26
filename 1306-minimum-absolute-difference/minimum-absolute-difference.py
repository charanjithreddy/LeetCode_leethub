class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort();
        min_abs_diff=float('inf');
        d={};
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i];
            if(diff in d):
                d[diff].append([arr[i],arr[i+1]]);
            else:
                d[diff]=[[arr[i],arr[i+1]]];
            min_abs_diff=min(min_abs_diff,diff);
        return d[min_abs_diff]
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """