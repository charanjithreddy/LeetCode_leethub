class Solution(object):
    def stoneGame(self, piles):
        l=0;
        r=len(piles)-1;
        alice=0;
        bob=0
        while(l<r):
            if(piles[l]>piles[r]):
                alice+=piles[l];
                bob+=piles[r];
            else:
                alice+=piles[r];
                bob+=piles[l];
            l+=1;
            r-=1;
        return alice>bob

        """
        :type piles: List[int]
        :rtype: bool
        """
        