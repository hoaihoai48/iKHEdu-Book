#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

int dfs(int u) {
    visited[u] = true;
    int sz = 1;
    for (int v : adj[u]) {
        if (!visited[v]) sz += dfs(v);
    }
    return sz;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> comp_sizes;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            comp_sizes.push_back(dfs(i));
        }
    }

    long long total_pairs = 1LL * n * (n - 1) / 2;
    long long connected_pairs = 0;

    for (long long sz : comp_sizes) {
        connected_pairs += sz * (sz - 1) / 2;
    }

    cout << total_pairs - connected_pairs << "\n";
    return 0;
}
