#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int parent_node[MAXN], depth[MAXN], heavy[MAXN], head[MAXN], pos[MAXN];
int cur_pos = 0;

int dfs_hld(int u, int p, int d) {
    int size = 1;
    int max_c_size = 0;
    depth[u] = d;
    parent_node[u] = p;
    heavy[u] = -1;

    for (int v : adj[u]) {
        if (v != p) {
            int c_size = dfs_hld(v, u, d + 1);
            size += c_size;
            if (c_size > max_c_size) {
                max_c_size = c_size;
                heavy[u] = v;
            }
        }
    }
    return size;
}

void decompose(int u, int h) {
    head[u] = h;
    pos[u] = ++cur_pos;
    if (heavy[u] != -1) decompose(heavy[u], h);
    for (int v : adj[u]) {
        if (v != parent_node[u] && v != heavy[u]) decompose(v, v);
    }
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

    dfs_hld(1, 1, 0);
    decompose(1, 1);

    cout << "HLD Built Successfully\n";
    return 0;
}
