class Solution(object):
    def twoSum(self, numbers, target):
        d={};
        for i in range(len(numbers)):
            if(target-numbers[i] in d):
                return [d[target-numbers[i]]+1,i+1];
            d[numbers[i]]=i;
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """