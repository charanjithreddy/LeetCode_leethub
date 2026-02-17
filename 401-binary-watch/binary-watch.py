class Solution(object):
    def readBinaryWatch(self, turnedOn):
        hours={
            0:["0"],
            1:["1","2","4","8"],
            2:["3","5","6","9","10"],
            3:["7","11"]
        }
        minutes={};
        for i in range(60):
            b=bin(i)[2:];
            ones=b.count("1");
            s=str(i);
            if(len(s)==1):
                s="0"+s;
            if(ones in minutes):
                minutes[ones].append(s);
            else:
                minutes[ones]=[s];
        res=[];
        for i in hours:
            for j in minutes:
                if(i+j==turnedOn):
                    for hour in hours[i]:
                        for minute in minutes[j]:
                            res.append(hour+":"+minute);
        return res;

        """
        :type turnedOn: int
        :rtype: List[str]
        """
        