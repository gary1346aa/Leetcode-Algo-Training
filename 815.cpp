#define pb push_back
#define f first
#define s second
#include <queue>
using namespace std;

class Solution {
public:
    int BFS(vector<vector<int>> map, int S, int T){
        vector<pair<bool,int>> vis(map.size(),{false,-1});
        queue<int> q;
        
        vis[S] = {true,0};
        q.push(S);
            
        while(q.size()){
            
            int cur = q.front();
            q.pop();
            
            if (cur == T) return (vis[cur].s)/2;
            
            if (!map[cur].empty()){
                for(int i : map[cur])
                    if (!vis[i].f){
                        vis[i] = {true, vis[cur].s + 1};
                        q.push(i);
                    }
                map[cur].clear();
            }
        }
        
        return -1;
    }
    int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
        
        vector<int> s_routes;
        for (auto bus : routes)
            for (auto stop : bus)
                s_routes.pb(stop);
        
        sort(s_routes.begin(),s_routes.end());
        s_routes.resize(unique(s_routes.begin(),s_routes.end()) - s_routes.begin());
        
        
        for (auto & bus : routes)
            for (auto & stop : bus)
                stop = lower_bound(s_routes.begin(), s_routes.end(), stop) - s_routes.begin();
    
        S = lower_bound(s_routes.begin(), s_routes.end(),S) - s_routes.begin() + routes.size();
        T = lower_bound(s_routes.begin(), s_routes.end(),T) - s_routes.begin() + routes.size();
        
        int X = routes.size(), Y = s_routes.size();
        routes.resize(X+Y);
        
        for(int i = 0; i < X; i++){
            for(auto &v : routes[i]){
                v += X;
                routes[v].pb(i);
            }
        }
        
        return BFS(routes ,S ,T);
    }
};