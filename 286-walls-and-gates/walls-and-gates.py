class Solution(object):
    def wallsAndGates(self, rooms):
        m=len(rooms);
        n=len(rooms[0]);
        def func(i,j,dist):
            if(0<=i<m and 0<=j<n and rooms[i][j]!=0 and rooms[i][j]!=-1):
                if(dist>=rooms[i][j]):
                    return;
                rooms[i][j]=min(rooms[i][j],dist);
                func(i,j+1,1+dist)
                func(i,j-1,1+dist)
                func(i+1,j,1+dist)
                func(i-1,j,1+dist)
            else:
                return


        for i in range(m):
            for j in range(n):
                if(rooms[i][j]==0):
                    func(i,j+1,1)
                    func(i,j-1,1)
                    func(i+1,j,1)
                    func(i-1,j,1)
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        