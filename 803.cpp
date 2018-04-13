#define pb push_back
int parent[40001];
int size[40001];
int sgrid[40001];

class Solution {
public:
    int find(int i){
        if (parent[parent[i]] != i)
            parent[i] = find(parent[i]);
        return parent[i];
    }

    void dsu(int a,int b){
        int parent_a = find(a);
        int parent_b = find(b);
        if (parent_a == parent_b)
            return;
        else if(size[parent_a] >= size[parent_b] || parent_a == 0){
            size[parent_a] += size[parent_b];
            parent[parent_b] = parent_a;
        }
        else if(size[parent_a] <  size[parent_b] || parent_b == 0){
            size[parent_b] += size[parent_a];
            parent[parent_a] = parent_b;
        }
        return;
    }     
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        vector<int> sgrid,shits,ret;
        int row = grid.size(), col = grid[0].size();

        sgrid.pb(1);   
        size[0] = 1;
        parent[0] = 0;
        for (int i = 0;i < row; ++i)
            for (int j = 0;j < col; ++j)
                sgrid.pb(grid[i][j]);

        for (int i = 0;i < hits.size(); ++i){
            int ij = 1 + (col * hits[i][0]) + hits[i][1];
            if (sgrid[ij] == 0)
                shits.pb(-1);
            else{
                shits.pb(ij);
                sgrid[ij] = 0;
            }
        }

        for (int i = 1;i < sgrid.size(); ++i){
            if(sgrid[i] == 1){
                size[i] = 1;
                parent[i] = i;
                if ((i-1) / col == 0)
                    dsu(0,i);
                if ((i-1) / col > 0)
                    if (sgrid[i - col] == 1)
                        dsu(i-col,i);
                if ((i-1) % col > 0)
                    if (sgrid[i - 1] == 1)
                        dsu(i-1,i);
            }
        }

        for (int x = shits.size() - 1; x >= 0; --x){
            if (shits[x] == -1)
                ret.insert(ret.begin(),0);
            else{
                int i = shits[x];
                int old_size = size[0], new_size;
                sgrid[i] = 1;
                parent[i] = i;
                size[i] = 1;
                
                if ((i-1)/col == 0)
                    dsu(0,i);
                if ((i-1)/col < row - 1)
                    if(sgrid[i + col] == 1)
                        dsu(i,i+col);
                if ((i-1)/col > 0)
                    if(sgrid[i - col] == 1)
                        dsu(i-col,i);
                if ((i-1)%col < col - 1)
                    if(sgrid[i + 1] == 1)
                        dsu(i,i+1);
                if ((i-1)%col > 0)
                    if(sgrid[i - 1] == 1)
                        dsu(i-1,i);

                if (find(i) == 0){
                    new_size = size[0];
                    ret.insert(ret.begin(),(new_size - old_size - 1));
                }
                else
                    ret.insert(ret.begin(),0);
            }
        }
        return ret;
    }
};