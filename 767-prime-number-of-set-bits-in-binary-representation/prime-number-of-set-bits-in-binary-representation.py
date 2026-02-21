class Solution(object):
    def countPrimeSetBits(self, left, right):
        s=set();
        for i in range(2,int(math.ceil(math.log(right,2)))+2):
            j=2;
            flag=0;
            while(j*j<=i):
                if(i%j==0):
                    flag=1;
                    break;
                j+=1;
            if(flag==0):
                s.add(i)
        res=0
        for i in range(left,right+1):
            if(bin(i)[2:].count("1") in s):
                res+=1;
        return res;
        """
        :type left: int
        :type right: int
        :rtype: int
        """