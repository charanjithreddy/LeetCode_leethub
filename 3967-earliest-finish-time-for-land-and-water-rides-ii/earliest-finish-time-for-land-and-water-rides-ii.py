class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        l=[];
        for i in range(len(landStartTime)):
            l.append(landStartTime[i]+landDuration[i]);
        w=[];
        for i in range(len(waterStartTime)):
            w.append(waterStartTime[i]+waterDuration[i]);
        res=float("inf");
        land=min(l);
        for i in range(len(waterStartTime)):
            if(waterStartTime[i]<land):
                res=min(res,land+waterDuration[i]);
            else:
                res=min(res,waterStartTime[i]+waterDuration[i]);
        water=min(w);
        for i in range(len(landStartTime)):
            if(landStartTime[i]<water):
                res=min(res,water+landDuration[i]);
            else:
                res=min(res,landStartTime[i]+landDuration[i]);
        return res
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        