#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        if (u < 1 || u > N || v < 1 || v > N) continue;
        adj[u].push_back(v); adj[v].push_back(u);
    }
    vector<int> col(N + 1, -1);
    queue<int> q;
    for (int s = 1; s <= N; s++) {
        if (col[s] != -1) continue;
        col[s] = 0; q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (col[v] == -1) { col[v] = col[u] ^ 1; q.push(v); }
                else if (col[v] == col[u]) { cout << "NO\n"; return 0; }
            }
        }
    }
    cout << "YES\n";
    return 0;
}
