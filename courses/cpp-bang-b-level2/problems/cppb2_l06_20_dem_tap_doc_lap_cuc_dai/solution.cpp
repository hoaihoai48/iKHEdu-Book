#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> adj(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v; --u; --v;
        adj[u] |= (1 << v); adj[v] |= (1 << u);
    }
    int max_sz = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                if (adj[i] & mask) { ok = false; break; }
            }
        }
        if (ok) max_sz = max(max_sz, __builtin_popcount(mask));
    }
    cout << max_sz << "\n";
    return 0;
}
