class Solution(object):
    def maxArea(self, height):
        o=0;
        left=0;
        right=len(height)-1;
        while(left<right):
            if(height[left]<height[right]):
                area=(right-left)*height[left];
                if(area>o):
                    o=area;
                left+=1;
            else:
                area=(right-left)*height[right];
                if(area>o):
                    o=area;
                right-=1;
        return o;
        """
        :type height: List[int]
        :rtype: int
        """