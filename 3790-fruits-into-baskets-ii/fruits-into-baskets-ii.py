class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        visited=[0]*len(fruits);
        c=0;
        for i in fruits:
            for j in range(len(fruits)):
                if(visited[j]==0 and i<=baskets[j]):
                    visited[j]=1;
                    break;            
        return visited.count(0);
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """