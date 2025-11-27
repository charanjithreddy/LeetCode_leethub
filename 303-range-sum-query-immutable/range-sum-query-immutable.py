class NumArray(object):

    def __init__(self, nums):
        self.nums=[0];
        for i in nums:
            self.nums.append(self.nums[-1]+i);
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        return self.nums[right+1]-self.nums[left];
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)