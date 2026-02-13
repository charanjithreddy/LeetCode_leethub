class Solution(object):
    def kClosest(self, points, k):
        arr=[];
        heapq.heapify(arr);
        for i in points:
            dist=i[0]*i[0]+i[1]*i[1]
            heapq.heappush(arr,(dist,i));
        res=[];
        while(len(res)<k):
            res.append(heapq.heappop(arr)[1]);
        return res;
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """