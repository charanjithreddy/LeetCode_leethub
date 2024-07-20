class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        output=0;
        for i in arr1:
            o=True;
            for j in arr2:
                if(abs(i-j)<=d):
                    o=False;
                    break;
            if(o==True):
                output+=1;
        return output;