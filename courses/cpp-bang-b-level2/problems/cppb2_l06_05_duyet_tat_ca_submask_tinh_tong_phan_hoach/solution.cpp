#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> cost(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> cost[i][j];
    }

    vector<int> dp(1 << n, INF);
    dp[0] = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        int p = __builtin_popcount(mask);
        if (p >= n) continue;

        for (int j = 0; j < n; ++j) {
            if (!((mask >> j) & 1)) {
                dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + cost[p][j]);
            }
        }
    }

    cout << dp[(1 << n) - 1] << "\n";
    return 0;
}
