#include <bits/stdc++.h>
using namespace std;
struct Frame { int v, pe; size_t idx; };
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<vector<pair<int,int>>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        if (u < 1 || u > N || v < 1 || v > N) continue;
        adj[u].push_back({v, i}); adj[v].push_back({u, i});
    }
    vector<int> disc(N + 1, -1), low(N + 1, 0), parent(N + 1, -1);
    vector<char> isArt(N + 1, 0), isBridge(max(0, M), 0);
    int timer = 0;
    for (int s = 1; s <= N; s++) {
        if (disc[s] != -1) continue;
        disc[s] = low[s] = timer++;
        int rootCh = 0;
        vector<Frame> st; st.push_back({s, -1, 0});
        while (!st.empty()) {
            Frame &f = st.back();
            int v = f.v;
            if (f.idx < adj[v].size()) {
                auto [to, id] = adj[v][f.idx++];
                if (id == f.pe) continue;
                if (disc[to] == -1) {
                    parent[to] = v;
                    if (v == s) rootCh++;
                    disc[to] = low[to] = timer++;
                    st.push_back({to, id, 0});
                } else {
                    low[v] = min(low[v], disc[to]);
                }
            } else {
                int p = parent[v];
                if (p != -1) {
                    low[p] = min(low[p], low[v]);
                    if (low[v] > disc[p]) isBridge[f.pe] = 1;
                    if (parent[p] != -1 && low[v] >= disc[p]) isArt[p] = 1;
                } else if (rootCh > 1) isArt[v] = 1;
                st.pop_back();
            }
        }
    }
    int ca = 0, cb = 0;
    for (int i = 1; i <= N; i++) ca += isArt[i];
    for (int i = 0; i < M; i++) cb += isBridge[i];
    cout << ca << ' ' << cb << "\n";
    return 0;
}
