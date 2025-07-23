class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1;
        c=((digits[i])+1)//10;
        digits[i]=(digits[i]+1)%10;
        i-=1;
        while(c>0 and i>-1):
            c=((digits[i])+1)//10;
            digits[i]=(digits[i]+1)%10
            i-=1;
        if(c>0):
            return [c]+digits;
        else:
            return digits;
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        