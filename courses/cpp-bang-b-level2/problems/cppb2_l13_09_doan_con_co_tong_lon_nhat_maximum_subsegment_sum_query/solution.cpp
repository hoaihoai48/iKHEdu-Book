#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int tin[MAXN], tout[MAXN], timer = 0;

void dfs_euler(int u, int p) {
    tin[u] = ++timer;
    for (int v : adj[u]) if (v != p) dfs_euler(v, u);
    tout[u] = timer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_euler(1, 0);

    for (int i = 1; i <= n; ++i) {
        cout << "Node " << i << ": [" << tin[i] << ", " << tout[i] << "]\n";
    }
    return 0;
}
