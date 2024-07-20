class Solution(object):
    def peakIndexInMountainArray(self, arr):
        start=0;
        end=len(arr)-1;
        index=-1;
        while(start<=end):
            mid=(start+end)//2;
            if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                index=mid;
                break;
            elif(arr[mid]<arr[mid+1]):
                start=mid+1;
            else:
                end=mid-1;
        return index;
        """
        :type arr: List[int]
        :rtype: int
        """
        