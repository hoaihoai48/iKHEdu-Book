#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    vector<long long> dist(n + 1, 1e18);
    vector<int> cnt(n + 1, 0);
    vector<bool> in_q(n + 1, false);
    queue<int> q;

    dist[s] = 0;
    q.push(s);
    in_q[s] = true;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        in_q[u] = false;

        for (const auto &e : adj[u]) {
            if (dist[u] + e.w < dist[e.to]) {
                dist[e.to] = dist[u] + e.w;
                if (!in_q[e.to]) {
                    q.push(e.to);
                    in_q[e.to] = true;
                    if (++cnt[e.to] > n) {
                        cout << "-1\n"; // Có chu trình âm
                        return 0;
                    }
                }
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << (dist[i] >= 1e18 ? -1 : dist[i]) << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
