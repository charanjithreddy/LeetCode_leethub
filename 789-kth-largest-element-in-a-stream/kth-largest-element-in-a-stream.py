class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k;
        self.nums=nums;
        """
        :type k: int
        :type nums: List[int]
        """
        

    def add(self, val):
        self.nums.append(val);
        self.nums.sort();
        return self.nums[len(self.nums)-self.k];
        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)