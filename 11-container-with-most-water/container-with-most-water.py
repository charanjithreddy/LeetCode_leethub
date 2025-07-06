class Solution(object):
    def maxArea(self, height):
        o=0;
        left=0;
        right=len(height)-1;
        while(left<right):
            area=(right-left)*min(height[left],height[right]);
            if(area>o):
                o=area;
            if(height[left]<height[right]):
                left+=1;
            else:
                right-=1;
        return o;
        """
        :type height: List[int]
        :rtype: int
        """