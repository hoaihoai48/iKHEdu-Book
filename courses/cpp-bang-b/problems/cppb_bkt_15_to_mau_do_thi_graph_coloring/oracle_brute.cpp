#include <bits/stdc++.h>
using namespace std;
int V, E, K;
vector<int> adj[15];
int color[15];
bool ok = false;
bool safe(int u, int c) {
    for (int v : adj[u]) if (color[v] == c) return false;
    return true;
}
void bkt(int u) {
    if (ok) return;
    if (u > V) { ok = true; return; }
    for (int c = 1; c <= K; ++c) {
        if (safe(u, c)) {
            color[u] = c;
            bkt(u + 1);
            color[u] = 0;
            if (ok) return;
        }
    }
}
int main() {
    if (!(cin >> V >> E >> K)) return 0;
    for (int i = 0; i < E; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    bkt(1);
    cout << (ok ? "YES\n" : "NO\n");
    return 0;
}
