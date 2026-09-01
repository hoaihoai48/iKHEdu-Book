#include <bits/stdc++.h>
using namespace std;

// Profile DP / DP Broken Profile lát gạch 1x2 trên lưới NxM
int dp[2][1 << 12];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n < m) swap(n, m);

    dp[0][0] = 1;
    int cur = 0, next = 1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            memset(dp[next], 0, sizeof(dp[next]));
            for (int mask = 0; mask < (1 << m); ++mask) {
                if (!dp[cur][mask]) continue;

                if (mask & (1 << j)) {
                    // Ô đã bị chiếm bởi gạch dọc từ trên xuống
                    dp[next][mask ^ (1 << j)] += dp[cur][mask];
                } else {
                    // Đặt gạch dọc xuống dưới
                    dp[next][mask | (1 << j)] += dp[cur][mask];

                    // Đặt gạch ngang sang phải
                    if (j + 1 < m && !(mask & (1 << (j + 1)))) {
                        dp[next][mask] += dp[cur][mask];
                    }
                }
            }
            swap(cur, next);
        }
    }

    cout << dp[cur][0] << "\n";
    return 0;
}
