class TimeMap(object):

    def __init__(self):
        self.d={};

    def set(self, key, value, timestamp):
        if(key in self.d):
            self.d[key].append([value,timestamp]);
        else:
            self.d[key]=[[value,timestamp]];
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        

    def get(self, key, timestamp):
        if(key not in self.d):
            return "";
        else:  
            res="";
            l=list(self.d[key]);
            left=0;
            right=len(l)-1;
            while(left<=right):
                mid=(left+right)//2;
                if(l[mid][1]<=timestamp):
                    res=l[mid][0]
                    left=mid+1;
                else:
                    right=mid-1
            return res

        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)