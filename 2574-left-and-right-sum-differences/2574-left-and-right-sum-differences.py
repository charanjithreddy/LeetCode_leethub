class Solution(object):
    def leftRightDifference(self, nums):
        answer=[];
        right=sum(nums);
        left=0;
        for i in nums:
            answer.append(abs(right-left-i));
            left+=i;
            right-=i;
        return answer;
    """
    :type nums: List[int]
    :rtype: List[int]
    """
        