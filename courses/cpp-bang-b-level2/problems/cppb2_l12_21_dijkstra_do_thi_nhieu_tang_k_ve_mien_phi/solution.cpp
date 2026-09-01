#include <bits/stdc++.h>
using namespace std;

// Dijkstra đồ thị nhiều tầng: dist[u][used_k]
const long long INF = 1e18;

struct State {
    long long d;
    int u, k;
    bool operator>(const State& o) const { return d > o.d; }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, K;
    if (!(cin >> n >> m >> K)) return 0;

    vector<vector<pair<int, long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<vector<long long>> dist(n + 1, vector<long long>(K + 1, INF));
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[1][0] = 0;
    pq.push({0, 1, 0});

    while (!pq.empty()) {
        auto [d, u, used] = pq.top();
        pq.pop();

        if (d > dist[u][used]) continue;

        for (auto edge : adj[u]) {
            int v = edge.first;
            long long w = edge.second;

            // Không dùng vé
            if (dist[u][used] + w < dist[v][used]) {
                dist[v][used] = dist[u][used] + w;
                pq.push({dist[v][used], v, used});
            }

            // Dùng 1 vé miễn phí (nếu còn)
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
