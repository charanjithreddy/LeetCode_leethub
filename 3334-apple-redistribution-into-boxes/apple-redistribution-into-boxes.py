class Solution(object):
    def minimumBoxes(self, apple, capacity):
        capacity.sort();
        capacity=capacity[::-1];
        s=0;
        res=0;
        for i in range(len(capacity)):
            s+=capacity[i];
            res+=1;
            if(s>=sum(apple)):
                break;
        return res;

        
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        