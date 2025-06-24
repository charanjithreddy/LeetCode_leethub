class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        o=[];
        l=len(nums);
        for i in range(l):
            if(nums[i]==key):
                if(len(o)==0):
                    x=max(0,i-k);
                    if(x<i):
                        for j in range(x,i):
                            o.append(j);
                else:
                    x=max(0,i-k,o[-1]+1);
                    if(x<i):
                        for j in range(x,i):
                            o.append(j);
                if(len(o)==0):
                    o.append(i);
                elif(i>o[-1]):
                    o.append(i);
                x=min(l-1,i+k);
                for j in range(max(i+1,o[-1]+1),x+1):
                    o.append(j);
        return o;
                

        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        