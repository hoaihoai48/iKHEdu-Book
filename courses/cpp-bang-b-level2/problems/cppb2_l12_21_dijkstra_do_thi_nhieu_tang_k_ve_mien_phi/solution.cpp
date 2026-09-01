#include <bits/stdc++.h>
using namespace std;

// Dijkstra nhiều tầng dùng priority_queue<vector<long long>>
const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, K;
    if (!(cin >> n >> m >> K)) return 0;

    vector<vector<vector<long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<vector<long long>> dist(n + 1, vector<long long>(K + 1, INF));
    priority_queue<vector<long long>, vector<vector<long long>>, greater<vector<long long>>> pq;

    dist[1][0] = 0;
    pq.push({0, 1, 0}); // {d, u, used_k}

    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();
        long long d = top[0], u = top[1], used = top[2];

        if (d > dist[u][used]) continue;

        for (const auto& edge : adj[u]) {
            int v = edge[0];
            long long w = edge[1];

            if (dist[u][used] + w < dist[v][used]) {
                dist[v][used] = dist[u][used] + w;
                pq.push({dist[v][used], v, used});
            }

            if (used < K && dist[u][used] < dist[v][used + 1]) {
                dist[v][used + 1] = dist[u][used];
                pq.push({dist[v][used + 1], v, used + 1});
            }
        }
    }

    long long ans = INF;
    for (int k = 0; k <= K; ++k) ans = min(ans, dist[n][k]);
    cout << (ans == INF ? -1 : ans) << "\n";
    return 0;
}
