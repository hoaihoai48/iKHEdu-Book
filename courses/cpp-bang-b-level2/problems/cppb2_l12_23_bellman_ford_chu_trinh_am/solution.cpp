#include <bits/stdc++.h>
using namespace std;

// Bellman-Ford dùng vector<vector<long long>> {u, v, w}
const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> edges(m, vector<long long>(3));
    for (int i = 0; i < m; ++i) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    vector<long long> dist(n + 1, 0);

    for (int i = 1; i <= n - 1; ++i) {
        for (const auto& e : edges) {
            int u = e[0], v = e[1];
            long long w = e[2];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    bool has_neg_cycle = false;
    for (const auto& e : edges) {
        int u = e[0], v = e[1];
        long long w = e[2];
        if (dist[u] + w < dist[v]) {
            has_neg_cycle = true;
            break;
        }
    }

    cout << (has_neg_cycle ? "YES\n" : "NO\n");
    return 0;
}
