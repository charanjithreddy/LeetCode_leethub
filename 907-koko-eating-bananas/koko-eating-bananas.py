class Solution(object):
    def minEatingSpeed(self, piles, h):
        left=1;
        right=max(piles);
        res=max(piles);
        while(left<=right):
            mid=(left+right)//2;
            o=0;
            for i in piles:
                if(i<mid):
                    o+=1;
                else:
                    if(i%mid==0):
                        o+=i//mid;
                    else:
                        o+=i//mid+1;
            if(o<=h):
                res=min(mid,res);
                right=mid-1;
            else:
                left=mid+1;
        return res;
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """