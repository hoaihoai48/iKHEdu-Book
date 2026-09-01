#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int tin[MAXN], low[MAXN], timer;
bool is_cut[MAXN];
int bridge_count = 0;

void dfs(int u, int p = -1) {
    tin[u] = low[u] = ++timer;
    int children = 0;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (tin[v]) {
            low[u] = min(low[u], tin[v]);
        } else {
            dfs(v, u);
            low[u] = min(low[u], low[v]);
            if (low[v] > tin[u]) bridge_count++;
            if (low[v] >= tin[u] && p != -1) is_cut[u] = true;
            children++;
        }
    }
    if (p == -1 && children > 1) is_cut[u] = true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs(i);
    }

    int cut_count = 0;
    for (int i = 1; i <= n; ++i) {
        if (is_cut[i]) cut_count++;
    }

    cout << cut_count << " " << bridge_count << "\n";
    return 0;
}
