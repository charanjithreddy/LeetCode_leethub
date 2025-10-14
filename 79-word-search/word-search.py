class Solution(object):
    def exist(self, board, word):
        res=[False];
        m=len(board);
        n=len(board[0]);
        total=m*n;
        visited=[];
        for i in range(m):
            t=[];
            for j in range(n):
                t.append(0);
            visited.append(t);
        
        def func(i,r,c,visited):
            if(i==len(word)):
                return;
            if(board[r][c]==word[i]):
                visited[r][c]=1;
                if(i==len(word)-1):
                    res[0]=True;
                    return;
                if(r+1<m and board[r+1][c]==word[i+1] and visited[r+1][c]==0):
                    func(i+1,r+1,c,visited);
                if(r-1>=0 and board[r-1][c]==word[i+1] and visited[r-1][c]==0):
                    func(i+1,r-1,c,visited);
                if(c+1<n and board[r][c+1]==word[i+1] and visited[r][c+1]==0):
                    func(i+1,r,c+1,visited);
                if(c-1>=0 and board[r][c-1]==word[i+1] and visited[r][c-1]==0):
                    func(i+1,r,c-1,visited);
                visited[r][c]=0;
            else:
                return;
        for i in range(m):
            for j in range(n):
                func(0,i,j,visited);
        return res[0];
        
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        