class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<List<Character>> rows=new ArrayList<>();
        for(int i=0;i<9;i++){
            rows.add(new ArrayList<>());
        }
        ArrayList<ArrayList<Character>> cols=new ArrayList<>();
        for(int i=0;i<9;i++){
            cols.add(new ArrayList<>());
        }
        ArrayList<ArrayList<ArrayList<Character>>> boxes=new ArrayList<>();
        for(int i=0;i<3;i++){
            ArrayList<ArrayList<Character>> temp=new ArrayList<>();
            for(int j=0;j<3;j++){
                temp.add(new ArrayList<>());
            }
            boxes.add(temp);
        }
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]=='.'){
                    continue;
                }
                if(rows.get(i).contains(board[i][j]) || cols.get(j).contains(board[i][j]) || boxes.get(i/3).get(j/3).contains(board[i][j])){
                    return false;
                }
                rows.get(i).add(board[i][j]);
                cols.get(j).add(board[i][j]);
                boxes.get(i/3).get(j/3).add(board[i][j]);
            }
        }
        return true;


        
    }
}