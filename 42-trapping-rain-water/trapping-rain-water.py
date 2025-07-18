class Solution(object):
    def trap(self, height):
        leftmax=height[0];
        rightmax=height[-1];
        l=0;
        r=len(height)-1;
        o=0;
        while(l<r):
            if(leftmax<rightmax):
                l+=1;
                leftmax=max(leftmax,height[l]);
                o+=leftmax-height[l];
            else:
                r-=1;
                rightmax=max(rightmax,height[r]);
                o+=rightmax-height[r];
        return o;
        """
        :type height: List[int]
        :rtype: int
        """