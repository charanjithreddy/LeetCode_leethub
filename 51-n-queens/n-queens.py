class Solution(object):
    def solveNQueens(self, n):
        res=[];
        def safe(i,j,board):
            for c in range(j):
                if(board[i][c]=='Q'):
                    return False;
            r=i-1;
            c=j-1;
            while(r>=0 and c>=0):
                if(board[r][c]=='Q'):
                    return False;
                r-=1;
                c-=1;
            r=i+1;
            c=j-1;
            while(r<n and c>=0):
                if(board[r][c]=='Q'):
                    return  False;
                r+=1;
                c-=1;
            return True;
        def printf(board):
            for i in board:
                print(i);
            print();
            
        def place(col,board):
            if(col==n):
                res.append([''.join(row) for row in board]);
                return;
            for r in range(n):
                if(safe(r,col,board)):
                    board[r][col]='Q';
                    printf(board)
                    place(col+1,board);
                    board[r][col]='.';
        place(0,[['.' for i in range(n)] for i in range(n)]);
        return res;
        """
        :type n: int
        :rtype: List[List[str]]
        """