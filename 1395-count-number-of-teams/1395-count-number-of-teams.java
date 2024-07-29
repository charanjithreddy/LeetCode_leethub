class Solution {
    public int numTeams(int[] rating) {
        int count=0;
        int l=rating.length;
        for(int i=0;i<l-2;i++){
            for(int j=i+1;j<l-1;j++){
                for(int k=j+1;k<l;k++){
                    if(rating[i]<rating[j]){
                        if(rating[j]<rating[k]){
                            count++;
                        }
                    }
                    else{
                        if(rating[j]>rating[k]){
                            count++;
                        }
                    }
                }
            }
        }
        return count;
    }
}