class Solution(object):
    def judgeCircle(self, moves):
        r=0;
        c=0;
        for i in moves:
            if(i=="R"):
                c+=1;
            if(i=="L"):
                c-=1;
            if(i=="U"):
                r+=1;
            if(i=="D"):
                r-=1;
        return r==0 and c==0
        """
        :type moves: str
        :rtype: bool
        """
        