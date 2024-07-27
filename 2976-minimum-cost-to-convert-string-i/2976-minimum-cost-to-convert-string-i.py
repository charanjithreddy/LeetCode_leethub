class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        matrix=[];
        for i in range(26):
            matrix.append([float('inf')]*26);
        for i in range(26):
            matrix[i][i]=0;
        for i in range(len(original)):
            a=ord(original[i])-97;
            b=ord(changed[i])-97;
            matrix[a][b]=min(cost[i],matrix[a][b]);
        for mid in range(26):
            for i in range(26):
                for j in range(26):
                    matrix[i][j]=min(matrix[i][j],matrix[i][mid]+matrix[mid][j]);
        count=0;
        for i in range(len(source)):
            if(matrix[ord(source[i])-97][ord(target[i])-97]==float('inf')):
                return -1;
            else:
                count+=matrix[ord(source[i])-97][ord(target[i])-97];
        return count;
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        