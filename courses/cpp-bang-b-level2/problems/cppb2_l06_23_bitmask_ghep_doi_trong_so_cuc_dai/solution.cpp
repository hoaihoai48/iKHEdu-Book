#include <bits/stdc++.h>
using namespace std;

// Bitmask DP ghép cặp trọng số lớn nhất
long long dp[1 << 20];
long long cost[20][20];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < 2 * n; ++i) {
        for (int j = 0; j < 2 * n; ++j) {
            cin >> cost[i][j];
        }
    }

    int total_nodes = 2 * n;
    memset(dp, 0, sizeof(dp));

    for (int mask = 0; mask < (1 << total_nodes); ++mask) {
        int i = 0;
        while (i < total_nodes && (mask & (1 << i))) i++;
        if (i == total_nodes) continue;

        for (int j = i + 1; j < total_nodes; ++j) {
            if (!(mask & (1 << j))) {
                int next_mask = mask | (1 << i) | (1 << j);
                dp[next_mask] = max(dp[next_mask], dp[mask] + cost[i][j]);
            }
        }
    }

    cout << dp[(1 << total_nodes) - 1] << "\n";
    return 0;
}
