class Solution(object):
    def maxNumberOfBalloons(self, text):
        d={};
        for i in "balloon":
            d[i]=0;
        for i in text:
            if(i in "balloon"):
                if(i=="l"or i=="o"):
                    d[i]+=0.5;
                else:
                    d[i]+=1;
        for i in d:
            d[i]=math.floor(d[i])
        return int(min(list(d.values())))
        """
        :type text: str
        :rtype: int
        """
        