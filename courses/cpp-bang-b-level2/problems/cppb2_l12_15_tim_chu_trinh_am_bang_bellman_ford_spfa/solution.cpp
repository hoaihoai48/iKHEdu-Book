#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<vector<pair<int,long long>>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; long long w; cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }
    vector<long long> dist(N + 1, 0);
    vector<int> cnt(N + 1, 0);
    vector<char> inq(N + 1, 1);
    queue<int> q;
    for (int i = 1; i <= N; i++) q.push(i);
    while (!q.empty()) {
        int u = q.front(); q.pop(); inq[u] = 0;
        for (auto [v, w] : adj[u]) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                if (!inq[v]) { inq[v] = 1; q.push(v); if (++cnt[v] >= N) { cout << "YES\n"; return 0; } }
            }
        }
    }
    cout << "NO\n";
    return 0;
}
