#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, const vector<vector<int>> &adj, const vector<long long> &val, vector<long long> &dp0, vector<long long> &dp1) {
    dp0[u] = 0;
    dp1[u] = val[u];
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, adj, val, dp0, dp1);
            dp0[u] += max(dp0[v], dp1[v]);
            dp1[u] += dp0[v];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> val(n + 1);
    for (int i = 1; i <= n; ++i) cin >> val[i];

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> dp0(n + 1, 0), dp1(n + 1, 0);
    dfs(1, 0, adj, val, dp0, dp1);

    cout << max(dp0[1], dp1[1]) << "\n";
    return 0;
}
