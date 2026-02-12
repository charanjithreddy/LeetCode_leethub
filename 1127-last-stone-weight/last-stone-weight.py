class Solution(object):
    def lastStoneWeight(self, stones):
        stones=[-i for i in stones];
        heapq.heapify(stones);
        while(len(stones)>1):
            y=-heapq.heappop(stones);
            x=-heapq.heappop(stones);
            if(x!=y):
                heapq.heappush(stones,x-y);
            else:
                heapq.heappush(stones,0)
        return -heapq.heappop(stones)

        """
        :type stones: List[int]
        :rtype: int
        """
        