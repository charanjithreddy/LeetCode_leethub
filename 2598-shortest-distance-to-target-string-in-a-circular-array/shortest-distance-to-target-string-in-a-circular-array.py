class Solution(object):
    def closestTarget(self, words, target, startIndex):
        i=0;
        n=len(words)
        while(i<n):
            if(words[(startIndex+i)%n]==target or words[(startIndex-i+n)%n]==target):
                return i;
            i+=1;
        return -1
                
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        