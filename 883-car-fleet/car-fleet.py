class Solution(object):
    def carFleet(self, target, position, speed):
        d={};
        for i in range(len(position)):
            d[position[i]]=(target-position[i])/float(speed[i]);
        pos=list(d.keys());
        pos.sort();
        stack=[];
        for i in range(len(pos)-1,-1,-1):
            if(len(stack)==0  or d[pos[i]]>stack[-1]):
                stack.append(d[pos[i]]);
        return len(stack);
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """