class Solution(object):
    def minOperations(self, logs):
        steps=0;
        for i in logs:
            if "." in i:
                if i=="../" and steps>0:
                    steps-=1;
            else:
                steps+=1;
        return steps;