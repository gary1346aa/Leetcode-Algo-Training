class Solution {
public:
    bool splitArraySameAverage(vector<int>& A) {
        
        int avg = accumulate(A.begin(), A.end(), 0);
        
        for (auto & i : A)
            i = i*A.size() - avg;

        

        int half = A.size()/2;
        vector<int> L(A.begin(),A.begin() + half);
        vector<int> R(A.begin() + half, A.end());
        
        map<int, int> lh;
        
        int Lall = accumulate(L.begin(), L.end(), 0);
        int Rall = accumulate(L.begin(), L.end(), 0);
        
        for(int sel = 0; sel < (1 << L.size()); sel++){
            
            int tmpl = 0;
            for(int i = 0; i < L.size(); i++)
                tmpl += ((sel & (1 << i)) > 0)*L[i];

            lh[tmpl] += 1;
        }

        int sol = 0;
        for(int sel = 0; sel < (1 << R.size()); sel++){
            
            int tmpr = 0;
            for(int i = 0; i < R.size(); i++)
                tmpr += ((sel & (1 << i)) > 0)*R[i];

            sol += lh[-tmpr];
        }

        return (sol > 2);
    }
};