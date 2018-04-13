class Solution {
public:
    int numTilings(int N) {
        long long a[1000] = {1,1,2};
        long long sum = 0;
        for (int i = 3; i <= N; ++i){
            sum  = (sum + a[i-3])%(1000000000+7);
            a[i] = (a[i-1] + a[i-2] + 2*sum)%(1000000000+7);
        }
        return a[N];
    }
};