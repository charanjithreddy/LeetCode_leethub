class Solution(object):
    def sequentialDigits(self, low, high):
        digit="123456789";
        t=[];
        for i in range(len(digit)):
            for j in range(i+1,len(digit)+1):
                t.append(int(digit[i:j]))
        res=[];
        for i in t:
            if(low<=i<=high):
                res.append(i);
        return sorted(res)
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        