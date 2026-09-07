#include <bits/stdc++.h>
using namespace std;
const long long INF = (long long)4e18;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M, S;
    if (!(cin >> N >> M >> S)) return 0;
    vector<vector<pair<int,long long>>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; long long w; cin >> u >> v >> w;
        adj[u].push_back({v, w}); adj[v].push_back({u, w});
    }
    vector<long long> d(N + 1, INF);
    d[S] = 0;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
    pq.push({0, S});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : adj[u])
            if (d[v] > du + w) { d[v] = du + w; pq.push({d[v], v}); }
    }
    for (int i = 1; i <= N; i++) { if (i > 1) cout << ' '; cout << (d[i] == INF ? -1 : d[i]); }
    cout << "\n";
    return 0;
}
