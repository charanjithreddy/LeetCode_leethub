class Solution(object):
    def numSteps(self, s):
        l=len(s);
        s=int(s,2);
        steps=0;
        while(s>1):
            if(s%2==0):
                s/=2;
                steps+=1;
            else:
                s+=1;
                steps+=1;
        return steps;