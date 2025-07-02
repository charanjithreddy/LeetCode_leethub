class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if(board[i][j]=="."):
                    board[i][j]=10;
                else:
                    board[i][j]=int(board[i][j]);
        for  i in board:
            a=[0]*10;
            for j in i:
                if(j<10):
                    a[j]+=1;
                    if(a[j]>1):
                        return False;
        for i in range(len(board)):
            x=[];
            for j in range(len(board)):
                x.append(board[j][i]);
            a=[0]*10;
            for j in x:
                if(j<10):
                    a[j]+=1;
                    if(a[j]>1):
                        return False;
        for i in range(3):
            for j in range(3):
                x=[];
                for r in range(3*i,(i+1)*3):
                    for c in range(3*j,(j+1)*3):
                        x.append(board[r][c]);
                a=[0]*10;
                for ele in x:
                    if(ele<10):
                        a[ele]+=1;
                        if(a[ele]>1):
                            return False;             
        return True;
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        