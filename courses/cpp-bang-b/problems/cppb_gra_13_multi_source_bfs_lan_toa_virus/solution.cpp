#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    if (n <= 0) return 0;

    vector<int> dist(n + 1, -1);
    queue<int> q;

    for (int i = 0; i < k; ++i) {
        int src;
        cin >> src;
        dist[src] = 0;
        q.push(src);
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int max_time = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        max_time = max(max_time, dist[u]);

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (dist[i] == -1) {
            cout << -1 << "\n";
            return 0;
        }
    }

    cout << max_time << "\n";
    return 0;
}
