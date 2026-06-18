class Solution(object):
    def angleClock(self, hour, minutes):
        theta=abs(30*hour-11.0*minutes/2);
        if(theta>180):
            return 360-theta
        else:
            return theta
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        