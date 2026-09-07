#include <bits/stdc++.h>
using namespace std;
const long long INF = (long long)4e18;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M, K;
    if (!(cin >> N >> M >> K)) return 0;
    vector<vector<pair<int,long long>>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; long long w; cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }
    vector<vector<long long>> dist(N + 1, vector<long long>(K + 1, INF));
    using State = tuple<long long,int,int>;
    priority_queue<State, vector<State>, greater<State>> pq;
    dist[1][0] = 0; pq.push({0, 1, 0});
    while (!pq.empty()) {
        auto [d, u, k] = pq.top(); pq.pop();
        if (d != dist[u][k]) continue;
        for (auto [v, w] : adj[u]) {
            if (dist[v][k] > d + w) { dist[v][k] = d + w; pq.push({dist[v][k], v, k}); }
            if (k < K && dist[v][k + 1] > d) { dist[v][k + 1] = d; pq.push({d, v, k + 1}); }
        }
    }
    long long ans = INF;
    for (int k = 0; k <= K; k++) ans = min(ans, dist[N][k]);
    cout << (ans == INF ? -1 : ans) << "\n";
    return 0;
}
