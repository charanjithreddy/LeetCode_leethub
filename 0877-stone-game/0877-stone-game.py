class Solution(object):
    def stoneGame(self, piles):
        alice=0;
        bob=0;
        while(len(piles)>0):
            if(piles[0]>piles[len(piles)-1]):
                alice+=piles[0];
                bob+=piles[len(piles)-1];
            else:
                alice+=piles[len(piles)-1];
                bob+=piles[0];
            piles.pop(0);
            piles.pop(len(piles)-1);
        if(alice>bob):
            return True;
        else:
            return False;