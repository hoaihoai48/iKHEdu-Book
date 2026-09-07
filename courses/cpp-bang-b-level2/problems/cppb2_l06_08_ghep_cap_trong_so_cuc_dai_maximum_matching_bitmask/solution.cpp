#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> w(n, vector<long long>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> w[i][j];
    vector<long long> dp(1 << n, 0);
    for (int mask = 0; mask < (1 << n); ++mask) {
        int i = 0;
        while (i < n && (mask & (1 << i))) ++i;
        if (i >= n) continue;
        for (int j = i + 1; j < n; ++j) {
            if (mask & (1 << j)) continue;
            dp[mask | (1 << i) | (1 << j)] = max(dp[mask | (1 << i) | (1 << j)], dp[mask] + w[i][j]);
        }
    }
    cout << dp[(1 << n) - 1] << "\n";
    return 0;
}
