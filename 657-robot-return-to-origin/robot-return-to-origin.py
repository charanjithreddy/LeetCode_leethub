class Solution(object):
    def judgeCircle(self, moves):
        r=0;
        l=0;
        u=0;
        d=0;
        for i in moves:
            if(i=="R"):
                r+=1;
            if(i=="L"):
                l+=1;
            if(i=="U"):
                u+=1;
            if(i=="D"):
                d+=1
        return r==l and u==d
        """
        :type moves: str
        :rtype: bool
        """
        