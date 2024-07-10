class Solution(object):
    def maxProduct(self, nums):
        h1=max(nums);
        nums.pop(nums.index(h1));
        return (h1-1)*(max(nums)-1)      