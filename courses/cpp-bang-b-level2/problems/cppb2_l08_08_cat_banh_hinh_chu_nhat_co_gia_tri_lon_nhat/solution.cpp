#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int W, H, n;
    if (!(cin >> W >> H >> n)) return 0;

    vector<vector<long long>> dp(W + 1, vector<long long>(H + 1, 0));

    for (int i = 0; i < n; ++i) {
        int w, h;
        long long val;
        cin >> w >> h >> val;
        if (w <= W && h <= H) dp[w][h] = max(dp[w][h], val);
        if (h <= W && w <= H) dp[h][w] = max(dp[h][w], val);
    }

    for (int i = 1; i <= W; ++i) {
        for (int j = 1; j <= H; ++j) {
            for (int k = 1; k < i; ++k) {
                dp[i][j] = max(dp[i][j], dp[k][j] + dp[i - k][j]);
            }
            for (int k = 1; k < j; ++k) {
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[i][j - k]);
            }
        }
    }

    cout << dp[W][H] << "\n";
    return 0;
}
