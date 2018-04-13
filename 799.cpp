class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        double stat[100][100] = {};
        stat[0][0] = poured;
    
        for (int i = 0; i <100; i++){
            for (int j = 0; j <= i; j++){
                if(stat[i][j]>1){
                    if (i+1 < 100){
                        stat[i+1][j] += (stat[i][j] - 1)/2;
                        stat[i+1][j+1] += (stat[i][j] - 1)/2;
                    }
                    stat[i][j] = 1;
                }
            }
        }
        return stat[query_row][query_glass];
    }
};