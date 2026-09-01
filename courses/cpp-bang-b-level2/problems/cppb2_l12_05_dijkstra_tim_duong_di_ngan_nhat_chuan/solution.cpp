#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> indeg(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        indeg[v]++;
    }

    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (indeg[i] == 0) q.push(i);
    }

    vector<int> topo;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        topo.push_back(u);
        for (int v : adj[u]) {
            if (--indeg[v] == 0) q.push(v);
        }
    }

    if ((int)topo.size() < n) {
        cout << "-1\n";
    } else {
        for (size_t i = 0; i < topo.size(); ++i) {
            cout << topo[i] << (i + 1 == topo.size() ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
