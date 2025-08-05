class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        visited=[0]*len(fruits);
        c=0;
        for i in fruits:
            j=0;
            while(j<len(baskets)):
                if(i<=baskets[j]):
                    baskets.pop(j);
                    break;
                j+=1;
        return len(baskets);
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """