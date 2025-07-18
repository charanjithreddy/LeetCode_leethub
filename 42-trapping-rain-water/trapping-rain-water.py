class Solution(object):
    def trap(self, height):
        left=[0];
        right=[0];
        m=0;
        for i in range(1,len(height)):
            m=max(m,height[i-1]);
            left.append(m);
        m=0;
        for i in range(len(height)-2,-1,-1):
            m=max(m,height[i+1]);
            right.insert(0,m);
        o=0;
        for i in range(len(height)):
            o+=max(0,min(left[i],right[i])-height[i]);
        return o;
        """
        :type height: List[int]
        :rtype: int
        """
        