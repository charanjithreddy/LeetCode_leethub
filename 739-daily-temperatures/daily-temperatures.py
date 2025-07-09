class Solution(object):
    def dailyTemperatures(self, temperatures):
        o=[0]*len(temperatures);
        stack=[];
        for index,value in enumerate(temperatures):
            while(len(stack)>0 and stack[-1][0]<value):
                o[stack[-1][1]]=index-stack[-1][1];
                stack.pop();
            stack.append([value,index])
        return o;
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """