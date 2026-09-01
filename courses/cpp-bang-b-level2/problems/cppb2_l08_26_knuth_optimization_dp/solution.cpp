#include <bits/stdc++.h>
using namespace std;

// Tối ưu hóa Knuth: opt[i][j-1] <= opt[i][j] <= opt[i+1][j] giảm O(N^3) -> O(N^2)
const long long INF = 1e18;
long long dp[1005][1005];
int opt[1005][1005];
long long a[1005], pref[1005];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
        opt[i][i] = i;
    }

    for (int len = 2; len <= n; ++len) {
        for (int i = 1; i <= n - len + 1; ++i) {
            int j = i + len - 1;
            dp[i][j] = INF;
            long long sum = pref[j] - pref[i - 1];

            for (int k = opt[i][j - 1]; k <= min(j - 1, opt[i + 1][j]); ++k) {
                long long cost = dp[i][k] + dp[k + 1][j] + sum;
                if (cost < dp[i][j]) {
                    dp[i][j] = cost;
                    opt[i][j] = k;
                }
            }
        }
    }

    cout << dp[1][n] << "\n";
    return 0;
}
