class Solution(object):
    def countDigits(self, num):
        t=num;
        count=0;
        while(t>0):
            if(num%(t%10)==0):
                count+=1;
            t=t/10;
        return count;