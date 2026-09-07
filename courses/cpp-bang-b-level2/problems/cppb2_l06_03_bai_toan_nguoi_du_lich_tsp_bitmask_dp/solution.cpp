#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> c(n, vector<long long>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> c[i][j];
    if (n == 1) {
        cout << 0 << "\n";
        return 0;
    }
    const long long INF = (long long)4e18;
    int full = (1 << n) - 1;
    vector<long long> dp((size_t)(full + 1) * n, INF);
    dp[1 * n + 0] = 0;
    for (int mask = 1; mask <= full; ++mask) {
        for (int u = 0; u < n; ++u) {
            if (!(mask & (1 << u))) continue;
            long long cur = dp[(size_t)mask * n + u];
            if (cur == INF) continue;
            for (int v = 0; v < n; ++v) {
                if (mask & (1 << v)) continue;
                long long &ref = dp[(size_t)(mask | (1 << v)) * n + v];
                ref = min(ref, cur + c[u][v]);
            }
        }
    }
    long long ans = INF;
    for (int u = 1; u < n; ++u)
        ans = min(ans, dp[(size_t)full * n + u] + c[u][0]);
    cout << ans << "\n";
    return 0;
}
