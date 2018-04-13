class Solution {
public:
    bool cal(int n, int L, int R){
        if (L == R)
            return false;
        int sum = 0, K =(L+R)/2;
        int tmp = K;
        while(tmp > 0){
            sum += tmp;
            tmp /= 5;
        }
        if (sum > n)
            return cal(n,L,K);
        else if (sum < n)
            return cal(n,K+1,R);
        else 
            return true;
    }
    int preimageSizeFZF(int K) {
        return 5*cal(K,0,K+1);
    }
};