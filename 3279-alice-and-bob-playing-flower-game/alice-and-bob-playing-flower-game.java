class Solution {
    public long flowerGame(int n, int m) {
        return (long)(n/2)*(m-m/2)+(long)(m/2)*(n-n/2);
    }
}