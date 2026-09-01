#include <bits/stdc++.h>
using namespace std;

// Dijkstra đa tiêu chí dùng vector<long long> {dist, edges, u} trong priority_queue mặc định
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<vector<long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    // Priority queue lưu {dist, edges_used, u}
    priority_queue<vector<long long>, vector<vector<long long>>, greater<vector<long long>>> pq;
    vector<long long> dist(n + 1, LLONG_MAX);

    dist[1] = 0;
    pq.push({0, 0, 1});

    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();
        long long d = top[0], edges = top[1], u = top[2];

        if (d > dist[u]) continue;

        for (const auto& edge : adj[u]) {
            int v = edge[0];
            long long w = edge[1];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], edges + 1, v});
            }
        }
    }

    cout << (dist[n] == LLONG_MAX ? -1 : dist[n]) << "\n";
    return 0;
}
