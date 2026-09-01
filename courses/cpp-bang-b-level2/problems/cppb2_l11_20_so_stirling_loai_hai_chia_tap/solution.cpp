#include <bits/stdc++.h>
using namespace std;

// S(n, k): Số cách phân hoạch tập n phần tử thành k tập con khác rỗng
const int MOD = 1000000007;
long long dp[1005][1005];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    dp[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j]) % MOD;
        }
    }

    cout << dp[n][k] << "\n";
    return 0;
}
