#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<vector<int>> g(N + 1), rg(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back(v); rg[v].push_back(u);
    }
    vector<char> vis(N + 1, 0);
    vector<int> order; order.reserve(N);
    for (int s = 1; s <= N; s++) {
        if (vis[s]) continue;
        vis[s] = 1;
        vector<pair<int,size_t>> st; st.push_back({s, 0});
        while (!st.empty()) {
            int v = st.back().first; size_t &k = st.back().second;
            if (k < g[v].size()) { int to = g[v][k++]; if (!vis[to]) { vis[to] = 1; st.push_back({to, 0}); } }
            else { order.push_back(v); st.pop_back(); }
        }
    }
    vector<char> done(N + 1, 0);
    int comp = 0;
    vector<int> stack2;
    for (int i = N - 1; i >= 0; i--) {
        int s = order[i];
        if (done[s]) continue;
        comp++;
        done[s] = 1; stack2.clear(); stack2.push_back(s);
        while (!stack2.empty()) {
            int v = stack2.back(); stack2.pop_back();
            for (int to : rg[v]) if (!done[to]) { done[to] = 1; stack2.push_back(to); }
        }
    }
    cout << comp << "\n";
    return 0;
}
