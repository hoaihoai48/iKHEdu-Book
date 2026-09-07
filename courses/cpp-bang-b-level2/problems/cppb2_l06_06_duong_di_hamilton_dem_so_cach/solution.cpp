#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        if (u < 0 || u >= n || v < 0 || v >= n) continue;
        adj[u].push_back(v);
    }
    int full = (1 << n) - 1;
    vector<long long> dp((size_t)(full + 1) * n, 0);
    dp[1 * n + 0] = 1;
    for (int mask = 1; mask <= full; ++mask) {
        for (int u = 0; u < n; ++u) {
            if (!(mask & (1 << u))) continue;
            long long cur = dp[(size_t)mask * n + u];
            if (cur == 0) continue;
            for (int v : adj[u]) {
                if (mask & (1 << v)) continue;
                dp[(size_t)(mask | (1 << v)) * n + v] += cur;
            }
        }
    }
    cout << dp[(size_t)full * n + (n - 1)] << "\n";
    return 0;
}
