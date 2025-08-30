class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> rows=new ArrayList<>();
        List<Set<Character>> cols=new ArrayList<>();
        List<Set<Character>> boxes=new ArrayList<>();
        for(int i=0;i<9;i++){
            rows.add(new HashSet<>());
            cols.add(new HashSet<>());
            boxes.add(new HashSet<>());
        }
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]=='.'){
                    continue;
                }
                if(rows.get(i).contains(board[i][j]) || cols.get(j).contains(board[i][j]) || boxes.get((i/3)*3 + (j/3)).contains(board[i][j])){
                    return false;
                }
                rows.get(i).add(board[i][j]);
                cols.get(j).add(board[i][j]);
                boxes.get((i/3)*3+(j/3)).add(board[i][j]);
            }
        }
        return true;
    }
}