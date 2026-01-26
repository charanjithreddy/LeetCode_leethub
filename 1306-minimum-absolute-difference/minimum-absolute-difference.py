class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort();
        min_abs_diff=float('inf');
        res=[];
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i];
            if(diff<min_abs_diff):
                min_abs_diff=diff
                res=[[arr[i],arr[i+1]]];
            elif(diff==min_abs_diff):
                res.append([arr[i],arr[i+1]]);
        return res;
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """