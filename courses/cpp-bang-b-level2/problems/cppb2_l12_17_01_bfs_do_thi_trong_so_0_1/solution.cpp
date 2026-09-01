#include <bits/stdc++.h>
using namespace std;

// 0-1 BFS tìm đường đi ngắn nhất bằng Deque O(V + E)
const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, start_node;
    if (!(cin >> n >> m >> start_node)) return 0;

    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> dist(n + 1, INF);
    deque<int> dq;

    dist[start_node] = 0;
    dq.push_front(start_node);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        for (auto edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << (dist[i] == INF ? -1 : dist[i]) << " ";
    }
    cout << "\n";
    return 0;
}
