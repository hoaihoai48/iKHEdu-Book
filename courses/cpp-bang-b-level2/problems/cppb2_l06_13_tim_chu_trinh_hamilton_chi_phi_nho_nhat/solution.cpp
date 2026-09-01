#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> w(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> w[i][j];
    }

    vector<vector<int>> dp(1 << n, vector<int>(n, INF));
    dp[1][0] = 0;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (dp[mask][u] >= INF) continue;
            for (int v = 0; v < n; ++v) {
                if (!((mask >> v) & 1)) {
                    dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + w[u][v]);
                }
            }
        }
    }

    int ans = INF;
    for (int u = 0; u < n; ++u) {
        ans = min(ans, dp[(1 << n) - 1][u] + w[u][0]);
    }

    cout << ans << "\n";
    return 0;
}
