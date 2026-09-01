#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) cin >> a[i][j];
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, -1e18));
    dp[1][1] = a[1][1];

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (i == 1 && j == 1) continue;
            long long best = -1e18;
            if (i > 1) best = max(best, dp[i - 1][j]);
            if (j > 1) best = max(best, dp[i][j - 1]);
            dp[i][j] = best + a[i][j];
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}
