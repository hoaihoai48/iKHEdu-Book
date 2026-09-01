#include <bits/stdc++.h>
using namespace std;

int timer = 0;
void dfs_bridge(int u, int p, const vector<vector<int>> &adj, vector<int> &tin, vector<int> &low, int &bridges) {
    tin[u] = low[u] = ++timer;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (tin[v]) {
            low[u] = min(low[u], tin[v]);
        } else {
            dfs_bridge(v, u, adj, tin, low, bridges);
            low[u] = min(low[u], low[v]);
            if (low[v] > tin[u]) bridges++;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> tin(n + 1, 0), low(n + 1, 0);
    int bridges = 0;

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs_bridge(i, 0, adj, tin, low, bridges);
    }

    cout << bridges << "\n";
    return 0;
}
