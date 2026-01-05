class Solution(object):
    def sumFourDivisors(self, nums):
        res=0;
        for i in nums:
            temp=0;
            cnt=0;
            j=1
            while(j*j<=i):
                if(i%j==0):
                    if(j!=(i/j)):
                        cnt+=2;
                        temp+=j;
                        temp+=(i/j);
                    else:
                        cnt+=1;
                        temp+=j;
                j+=1;
            if(cnt==4):
                res+=temp;
        return res;
        """
        :type nums: List[int]
        :rtype: int
        """
        