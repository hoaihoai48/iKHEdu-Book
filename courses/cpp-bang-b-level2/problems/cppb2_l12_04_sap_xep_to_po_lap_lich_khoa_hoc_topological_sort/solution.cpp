#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<vector<int>> adj(N + 1);
    vector<int> indeg(N + 1, 0);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); indeg[v]++;
    }
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 1; i <= N; i++) if (indeg[i] == 0) pq.push(i);
    vector<int> ans;
    while (!pq.empty()) {
        int u = pq.top(); pq.pop();
        ans.push_back(u);
        for (int v : adj[u]) if (--indeg[v] == 0) pq.push(v);
    }
    if ((int)ans.size() != N) { cout << -1 << "\n"; return 0; }
    for (int i = 0; i < N; i++) { if (i) cout << ' '; cout << ans[i]; }
    cout << "\n";
    return 0;
}
