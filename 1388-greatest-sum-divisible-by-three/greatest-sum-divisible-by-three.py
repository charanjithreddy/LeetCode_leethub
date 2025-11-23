class Solution(object):
    def maxSumDivThree(self, nums):
        total=0;
        one=float("inf");
        two=float("inf");
        for i in nums:
            total+=i;
            if(i%3==1):
                two=min(two,one+i);
                one=min(one,i);
            if(i%3==2):
                one=min(one,two+i);
                two=min(two,i);
        if(total%3==0):
            return total;
        elif(total%3==1):
            return total-one;
        else:
            return total-two;
        """
        :type nums: List[int]
        :rtype: int
        """