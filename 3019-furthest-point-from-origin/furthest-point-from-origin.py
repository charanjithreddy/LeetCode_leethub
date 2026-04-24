class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        L=0;
        R=0;
        d=0;
        for i in moves:
            if(i=="L"):
                L+=1;
            elif(i=="R"):
                R+=1;
            else:
                d+=1;
        return abs(L-R)+d
        """
        :type moves: str
        :rtype: int
        """
        