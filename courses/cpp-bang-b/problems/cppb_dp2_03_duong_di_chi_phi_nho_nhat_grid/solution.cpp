#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) cin >> a[i][j];
    }

    vector<long long> dp(m, INF);
    dp[0] = a[0][0];

    for (int j = 1; j < m; ++j) dp[j] = dp[j - 1] + a[0][j];

    for (int i = 1; i < n; ++i) {
        dp[0] += a[i][0];
        for (int j = 1; j < m; ++j) {
            dp[j] = min(dp[j], dp[j - 1]) + a[i][j];
        }
    }

    cout << dp[m - 1] << "\n";
    return 0;
}
