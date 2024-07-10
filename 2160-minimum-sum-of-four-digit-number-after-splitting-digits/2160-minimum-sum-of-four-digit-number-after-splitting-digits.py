class Solution(object):
    def minimumSum(self, num):
        n=[];
        for i in range(4):
            n.append(num%10);
            num/=10;
        n.sort();
        return 10*(n[0]+n[1])+n[2]+n[3];
        """
        :type num: int
        :rtype: int
        """
        