class Solution(object):
    def largestAltitude(self, gain):
        alt=0;
        s=0;
        for i in gain:
            s=s+i;
            if(s>alt):
                alt=s;
        return alt;

        """
        :type gain: List[int]
        :rtype: int
        """
        