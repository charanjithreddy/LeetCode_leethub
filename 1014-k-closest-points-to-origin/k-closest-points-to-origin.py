class Solution(object):
    def kClosest(self, points, k):
        arr=[];
        heapq.heapify(arr);
        d={};
        for i in points:
            dist=i[0]*i[0]+i[1]*i[1]
            if(dist in d):
                d[dist].append(i);
            else:
                d[dist]=[i];
            heapq.heappush(arr,dist);
        res=[];
        while(len(res)<k):
            res.extend(d[heapq.heappop(arr)]);
        return res;
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """