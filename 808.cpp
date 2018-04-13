class Solution {
public:
    double soupServings(int N) {
        if (N > 6000) return 1;
        N = N / 25 + (N % 25 > 0 ? 1 : 0);
        vector<vector<double>> DP(N + 1, vector<double>(N + 1, -1));
        DP[0][0] = 0.5;
        for (int i = 1; i < N + 1; i ++){
            DP[i][0] = 0;
            DP[0][i] = 1;
        }
        return dfs(DP,N,N);
    }
    double dfs(vector<vector<double>>& DP, int a, int b){
        if (DP[a][b] >= 0) return DP[a][b];
        else{
            double sum = 0;
            sum += dfs(DP, max(a - 4,0), b);
            sum += dfs(DP, max(a - 3,0), max(b - 1,0));
            sum += dfs(DP, max(a - 2,0), max(b - 2,0));
            sum += dfs(DP, max(a - 1,0), max(b - 3,0));
            DP[a][b] = sum/4 ; 
            return DP[a][b];
        }
    }
};
