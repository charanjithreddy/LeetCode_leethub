class Solution(object):
    def twoSum(self, numbers, target):
        begin=0;
        end=len(numbers)-1;
        while(begin<end):
            s=numbers[begin]+numbers[end]
            if(s==target):
                return [begin+1,end+1];
            elif(s<target):
                begin+=1;
            else:
                end-=1;
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        