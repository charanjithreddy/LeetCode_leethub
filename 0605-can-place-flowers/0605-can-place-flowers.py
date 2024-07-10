class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count=0;
        l=len(flowerbed);
        if(l>1 and flowerbed[0]==0 and flowerbed[1]==0):
            count+=1;
            flowerbed[0]=1;
        if(flowerbed[l-1]==0 and flowerbed[l-2]==0):
            count+=1;
            flowerbed[l-1]=1;

        for i in range(2,l-2):
            if(flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
                count+=1;
                flowerbed[i]=1;
        
        if(count>=n):
            return True;
        else:
            return False;


        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        