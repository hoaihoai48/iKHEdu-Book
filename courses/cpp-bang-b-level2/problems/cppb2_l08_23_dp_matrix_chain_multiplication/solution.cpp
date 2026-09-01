#include <bits/stdc++.h>
using namespace std;

// Quy hoạch động nhân chuỗi ma trận O(N^3)
long long dp[505][505];
long long p[505];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i <= n; ++i) cin >> p[i];

    for (int len = 2; len <= n; ++len) {
        for (int i = 1; i <= n - len + 1; ++i) {
            int j = i + len - 1;
            dp[i][j] = LLONG_MAX;
            for (int k = i; k < j; ++k) {
                long long cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }

    cout << dp[1][n] << "\n";
    return 0;
}
