#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, const vector<vector<int>> &adj, vector<long long> &diff) {
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, adj, diff);
            diff[u] += diff[v];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> diff(n + 1, 0);
    while (q--) {
        int node;
        long long val;
        cin >> node >> val;
        diff[node] += val;
    }

    dfs(1, 0, adj, diff);

    for (int i = 1; i <= n; ++i) {
        cout << diff[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
