#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v);
    }
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

    vector<int> leaders;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            leaders.push_back(i);
            dfs(i);
        }
    }

    int needed = leaders.size() - 1;
    cout << needed << "\n";
    for (int i = 0; i < needed; ++i) {
        cout << leaders[i] << " " << leaders[i + 1] << "\n";
    }
    return 0;
}
