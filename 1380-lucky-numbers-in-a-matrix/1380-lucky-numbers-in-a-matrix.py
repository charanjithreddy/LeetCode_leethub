class Solution(object):
    def luckyNumbers (self, matrix):
        o=[];
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]==min(matrix[i])):
                    s=[];
                    for k in range(len(matrix)):
                        s.append(matrix[k][j]);
                    if(matrix[i][j]==max(s)):
                        o.append(matrix[i][j]);
        return o;