#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, const vector<vector<int>> &adj, vector<bool> &matched, int &matching_size) {
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, adj, matched, matching_size);
        }
    }
    if (!matched[u] && p != 0 && !matched[p]) {
        matched[u] = matched[p] = true;
        matching_size++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> matched(n + 1, false);
    int matching_size = 0;
    dfs(1, 0, adj, matched, matching_size);

    cout << matching_size << "\n";
    return 0;
}
