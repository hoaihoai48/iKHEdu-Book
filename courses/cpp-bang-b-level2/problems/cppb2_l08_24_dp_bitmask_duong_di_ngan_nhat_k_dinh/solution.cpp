#include <bits/stdc++.h>
using namespace std;

// TSP / Bitmask DP đường đi ngắn nhất qua K đỉnh O(K^2 * 2^K + N*M)
const long long INF = 1e18;
long long dp[1 << 16][16];
long long dist_k[16][16];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            cin >> dist_k[i][j];
        }
    }

    for (int mask = 0; mask < (1 << k); ++mask) {
        for (int i = 0; i < k; ++i) dp[mask][i] = INF;
    }

    dp[1][0] = 0; // Bắt đầu từ đỉnh 0

    for (int mask = 1; mask < (1 << k); ++mask) {
        for (int u = 0; u < k; ++u) {
            if (dp[mask][u] == INF) continue;
            for (int v = 0; v < k; ++v) {
                if (!(mask & (1 << v))) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + dist_k[u][v]);
                }
            }
        }
    }

    long long ans = INF;
    for (int u = 0; u < k; ++u) ans = min(ans, dp[(1 << k) - 1][u]);
    cout << ans << "\n";
    return 0;
}
