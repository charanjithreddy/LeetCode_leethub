class Solution(object):
    def isValidSudoku(self, board):
        rows=[[] for i in range(9)];
        cols=[[] for i in range(9)];
        box=[[[],[],[]],[[],[],[]],[[],[],[]]];
        for r in range(9):
            for c in range(9):
                if(board[r][c]=="."):
                    continue;
                if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in box[r//3][c//3]):
                    return False;
                rows[r].append(board[r][c]);
                cols[c].append(board[r][c]);
                box[r//3][c//3].append(board[r][c]);
        return True;


        """
        :type board: List[List[str]]
        :rtype: bool
        """
        