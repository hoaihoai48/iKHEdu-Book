#include <bits/stdc++.h>
using namespace std;

// Bellman-Ford phát hiện chu trình âm O(V * E)
struct Edge {
    int u, v;
    long long w;
};

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    vector<long long> dist(n + 1, 0); // Tìm chu trình âm trên toàn đồ thị

    for (int i = 1; i <= n - 1; ++i) {
        for (const auto& e : edges) {
            if (dist[e.u] + e.w < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.w;
            }
        }
    }

    bool has_neg_cycle = false;
    for (const auto& e : edges) {
        if (dist[e.u] + e.w < dist[e.v]) {
            has_neg_cycle = true;
            break;
        }
    }

    cout << (has_neg_cycle ? "YES\n" : "NO\n");
    return 0;
}
