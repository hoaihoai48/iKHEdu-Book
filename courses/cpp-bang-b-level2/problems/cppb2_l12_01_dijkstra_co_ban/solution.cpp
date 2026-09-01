#include <bits/stdc++.h>
using namespace std;

void dfs(int u, const vector<vector<int>> &adj, vector<bool> &vis) {
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) dfs(v, adj, vis);
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

    vector<bool> vis(n + 1, false);
    int components = 0;

    for (int i = 1; i <= n; ++i) {
        if (!vis[i]) {
            components++;
            dfs(i, adj, vis);
        }
    }

    cout << components << "\n";
    return 0;
}
