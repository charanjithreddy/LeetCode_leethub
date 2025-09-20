class Solution(object):
    def largestRectangleArea(self, heights):
        res=heights[0];
        stack=[];
        for i in range(len(heights)):
            if(len(stack)==0):
                stack.append([i,heights[i]]);
            else:
                if(stack[-1][1]<=heights[i]):
                    stack.append([i,heights[i]]);
                else:
                    ind=i;
                    while(len(stack)>0 and stack[-1][1]>heights[i]):
                        res=max(res,(i-stack[-1][0])*stack[-1][1]);
                        ind=stack[-1][0];
                        stack.pop();
                    stack.append([ind,heights[i]]);
        while(len(stack)>0):
            res=max(res,(len(heights)-stack[-1][0])*stack[-1][1]);
            stack.pop();
        return res;       
        """
        :type heights: List[int]
        :rtype: int
        """