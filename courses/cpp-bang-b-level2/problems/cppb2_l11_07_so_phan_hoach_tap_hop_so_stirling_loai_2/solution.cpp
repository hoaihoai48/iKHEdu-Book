#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;

    if (s < n || s > 6 * n) {
        cout << "0.000000\n";
        return 0;
    }

    vector<double> dp(s + 1, 0.0);
    dp[0] = 1.0;

    for (int i = 1; i <= n; ++i) {
        vector<double> next_dp(s + 1, 0.0);
        for (int j = 1; j <= s; ++j) {
            for (int face = 1; face <= 6; ++face) {
                if (j >= face) next_dp[j] += dp[j - face] / 6.0;
            }
        }
        dp = next_dp;
    }

    cout << fixed << setprecision(6) << dp[s] << "\n";
    return 0;
}
