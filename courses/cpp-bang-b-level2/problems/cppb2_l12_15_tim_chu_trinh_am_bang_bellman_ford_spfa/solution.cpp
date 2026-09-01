#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50005;
vector<int> adj[MAXN];
int pair_u[MAXN], pair_v[MAXN], dist_u[MAXN];

bool bfs_hk(int n) {
    queue<int> q;
    for (int u = 1; u <= n; ++u) {
        if (pair_u[u] == 0) {
            dist_u[u] = 0;
            q.push(u);
        } else dist_u[u] = 1e9;
    }
    dist_u[0] = 1e9;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (dist_u[u] < dist_u[0]) {
            for (int v : adj[u]) {
                if (dist_u[pair_v[v]] == (int)1e9) {
                    dist_u[pair_v[v]] = dist_u[u] + 1;
                    q.push(pair_v[v]);
                }
            }
        }
    }
    return dist_u[0] != 1e9;
}

bool dfs_hk(int u) {
    if (u != 0) {
        for (int v : adj[u]) {
            if (dist_u[pair_v[v]] == dist_u[u] + 1) {
                if (dfs_hk(pair_v[v])) {
                    pair_v[v] = u;
                    pair_u[u] = v;
                    return true;
                }
            }
        }
        dist_u[u] = 1e9;
        return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, p;
    if (!(cin >> n >> m >> p)) return 0;

    for (int i = 0; i < p; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
    }

    int matching = 0;
    while (bfs_hk(n)) {
        for (int u = 1; u <= n; ++u) {
            if (pair_u[u] == 0 && dfs_hk(u)) matching++;
        }
    }

    cout << matching << "\n";
    return 0;
}
