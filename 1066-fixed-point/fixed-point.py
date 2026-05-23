class Solution(object):
    def fixedPoint(self, arr):
        for i in range(len(arr)):
            if(i==arr[i]):
                return i;
        return -1
        """
        :type arr: List[int]
        :rtype: int
        """
        