#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> adj[MAXN], adj_rev[MAXN];
vector<bool> vis;
vector<int> order, comp;

void dfs1(int u) {
    vis[u] = true;
    for (int v : adj[u]) if (!vis[v]) dfs1(v);
    order.push_back(u);
}

void dfs2(int u, int c) {
    comp[u] = c;
    for (int v : adj_rev[u]) if (comp[v] == -1) dfs2(v, c);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        int not_u = (u > 0 ? u + n : -u);
        int not_v = (v > 0 ? v + n : -v);
        int actual_u = (u > 0 ? u : -u + n);
        int actual_v = (v > 0 ? v : -v + n);

        adj[not_u].push_back(actual_v);
        adj[not_v].push_back(actual_u);
        adj_rev[actual_v].push_back(not_u);
        adj_rev[actual_u].push_back(not_v);
    }

    vis.assign(2 * n + 1, false);
    for (int i = 1; i <= 2 * n; ++i) if (!vis[i]) dfs1(i);

    comp.assign(2 * n + 1, -1);
    int c = 0;
    for (int i = 2 * n - 1; i >= 0; --i) {
        int u = order[i];
        if (comp[u] == -1) dfs2(u, c++);
    }

    for (int i = 1; i <= n; ++i) {
        if (comp[i] == comp[i + n]) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}
