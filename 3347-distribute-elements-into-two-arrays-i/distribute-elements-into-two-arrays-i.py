class Solution(object):
    def resultArray(self, nums):
        arr1=[nums[0]];
        arr2=[nums[1]];
        for i in nums[2:]:
            if(arr1[-1]>arr2[-1]):
                arr1.append(i);
            else:
                arr2.append(i);
        return arr1+arr2
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        