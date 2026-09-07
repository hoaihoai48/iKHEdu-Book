#include <bits/stdc++.h>
using namespace std;
const int INF = 2000000000;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M, S;
    if (!(cin >> N >> M >> S)) return 0;
    vector<vector<pair<int,int>>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v, w; cin >> u >> v >> w;
        adj[u].push_back({v, w}); adj[v].push_back({u, w});
    }
    vector<int> d(N + 1, INF);
    d[S] = 0;
    deque<int> dq; dq.push_front(S);
    while (!dq.empty()) {
        int u = dq.front(); dq.pop_front();
        for (auto [v, w] : adj[u])
            if (d[v] > d[u] + w) {
                d[v] = d[u] + w;
                if (w == 0) dq.push_front(v); else dq.push_back(v);
            }
    }
    for (int i = 1; i <= N; i++) { if (i > 1) cout << ' '; cout << (d[i] == INF ? -1 : d[i]); }
    cout << "\n";
    return 0;
}
