class Solution(object):
    def dailyTemperatures(self, temperatures):
        o=[0]*len(temperatures);
        stack=[];
        for i in range(len(temperatures)):
            while(len(stack)>0 and stack[-1][0]<temperatures[i]):
                o[stack[-1][1]]=i-stack[-1][1];
                stack.pop();
            stack.append([temperatures[i],i])
        return o;
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """