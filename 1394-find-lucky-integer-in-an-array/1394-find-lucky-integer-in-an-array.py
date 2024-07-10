class Solution(object):
    def findLucky(self, arr):
        count=-1;
        for i in set(arr):
            n=arr.count(i);
            if(n==i and n>count):
                count=arr.count(i);
        return count;