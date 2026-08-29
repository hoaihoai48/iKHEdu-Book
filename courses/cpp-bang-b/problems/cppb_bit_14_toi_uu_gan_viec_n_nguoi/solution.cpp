#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> cost(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> cost[i][j];
        }
    }

    int total_masks = (1 << n);
    const long long INF = 1e18;
    vector<long long> dp(total_masks, INF);
    dp[0] = 0;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (dp[mask] == INF) continue;
        int task_idx = __builtin_popcount(mask);
        if (task_idx >= n) continue;

        for (int j = 0; j < n; ++j) {
            if (!((mask >> j) & 1)) {
                int next_mask = mask | (1 << j);
                dp[next_mask] = min(dp[next_mask], dp[mask] + cost[task_idx][j]);
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
