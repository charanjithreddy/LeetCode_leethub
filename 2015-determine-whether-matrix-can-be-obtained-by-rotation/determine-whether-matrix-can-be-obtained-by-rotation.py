class Solution(object):
    def findRotation(self, mat, target):
        n=len(mat);
        for i in range(4):
            temp=[];
            for x in range(n):
                t=[];
                for y in range(n):
                    t.append(mat[y][x]);
                temp.append(t[::-1]);
            for x in range(n):
                for y in range(n):
                    mat[x][y]=temp[x][y];
            if(mat==target):
                return True;
        return False


        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        