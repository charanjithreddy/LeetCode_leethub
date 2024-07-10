class Solution(object):
    def simplifiedFractions(self, n):
        o=[];
        for i in range(2,n+1):
            for j in range(1,i):
                hcf=1;
                for x in range(1,j+1):
                    if(j%x==0 and i%x==0):
                        hcf=x;
                s=str(j/hcf)+"/"+str(i/hcf);
                o.append(s);
        return set(o);