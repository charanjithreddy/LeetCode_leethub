class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n=grid.length;
        ArrayList<Integer> temp=new ArrayList<Integer>();
        for(int i=n-1;i>=0;i--){
            int t=i;
            int j=0;
            ArrayList<Integer> arr=new ArrayList<Integer>();
            while(t<n){
                arr.add(grid[j][t]);
                t+=1;
                j+=1;

            }
            Collections.sort(arr);
            temp.addAll(arr);
        }
        for(int i=0;i<n;i++){
            int t=i;
            int j=0;
            ArrayList<Integer> arr=new ArrayList<Integer>();
            while(t<n){
                arr.add(grid[t][j]);
                t+=1;
                j+=1;
            }
            Collections.sort(arr,Collections.reverseOrder());
            temp.addAll(arr);
        }
        int ind=0;
        for(int i=n-1;i>=0;i--){
            int t=i;
            int j=0;
            while(t<n){
                grid[j][t]=temp.get(ind++);
                t+=1;
                j+=1;
            }
        }
        for(int i=0;i<n;i++){
            int t=i;
            int j=0;
            while(t<n){
                grid[t][j]=temp.get(ind++);
                t+=1;
                j+=1;
            }
        }
        return grid;        
    }
}