class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        hours.sort();
        if(target in  hours):
            s=hours.index(target);
            return len(hours)-s;
        else:
            count=0;
            for i in hours:
                if (i>=target):
                    count+=1;
            return count;
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        