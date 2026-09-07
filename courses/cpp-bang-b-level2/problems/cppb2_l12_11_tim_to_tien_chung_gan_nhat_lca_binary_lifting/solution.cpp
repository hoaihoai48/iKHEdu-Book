#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    if (!(cin >> N >> Q)) return 0;
    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }
    const int LOG = 18;
    vector<vector<int>> up(LOG, vector<int>(N + 1, 0));
    vector<int> dep(N + 1, 0);
    queue<int> q; q.push(1); up[0][1] = 1;
    vector<char> vis(N + 1, 0); vis[1] = 1;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) if (!vis[v]) { vis[v] = 1; dep[v] = dep[u] + 1; up[0][v] = u; q.push(v); }
    }
    for (int k = 1; k < LOG; k++)
        for (int v = 1; v <= N; v++) up[k][v] = up[k - 1][up[k - 1][v]];
    auto lca = [&](int a, int b) {
        if (dep[a] < dep[b]) swap(a, b);
        int d = dep[a] - dep[b];
        for (int k = 0; k < LOG; k++) if (d >> k & 1) a = up[k][a];
        if (a == b) return a;
        for (int k = LOG - 1; k >= 0; k--) if (up[k][a] != up[k][b]) { a = up[k][a]; b = up[k][b]; }
        return up[0][a];
    };
    while (Q--) { int u, v; cin >> u >> v; cout << lca(u, v) << "\n"; }
    return 0;
}
