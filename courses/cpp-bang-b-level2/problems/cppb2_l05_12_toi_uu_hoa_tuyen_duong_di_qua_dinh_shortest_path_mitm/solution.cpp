#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist_s(n + 1, -1), dist_t(n + 1, -1);
    queue<int> q;

    dist_s[s] = 0; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist_s[v] == -1) {
                dist_s[v] = dist_s[u] + 1;
                q.push(v);
            }
        }
    }

    dist_t[t] = 0; q.push(t);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist_t[v] == -1) {
                dist_t[v] = dist_t[u] + 1;
                q.push(v);
            }
        }
    }

    cout << dist_s[t] << "\n";
    return 0;
}
