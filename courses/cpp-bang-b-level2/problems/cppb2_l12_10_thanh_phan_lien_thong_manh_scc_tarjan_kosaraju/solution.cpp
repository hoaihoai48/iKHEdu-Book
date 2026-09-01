#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005, LOG = 20;
vector<int> adj[MAXN];
int up[MAXN][LOG], depth[MAXN];

void dfs_lca(int u, int p, int d) {
    depth[u] = d;
    up[u][0] = p;
    for (int j = 1; j < LOG; ++j) {
        up[u][j] = up[up[u][j - 1]][j - 1];
    }
    for (int v : adj[u]) {
        if (v != p) dfs_lca(v, u, d + 1);
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int j = LOG - 1; j >= 0; --j) {
        if (depth[u] - (1 << j) >= depth[v]) {
            u = up[u][j];
        }
    }
    if (u == v) return u;
    for (int j = LOG - 1; j >= 0; --j) {
        if (up[u][j] != up[v][j]) {
            u = up[u][j];
            v = up[v][j];
        }
    }
    return up[u][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_lca(1, 1, 0);

    while (q--) {
        int u, v; cin >> u >> v;
        cout << get_lca(u, v) << "\n";
    }
    return 0;
}
