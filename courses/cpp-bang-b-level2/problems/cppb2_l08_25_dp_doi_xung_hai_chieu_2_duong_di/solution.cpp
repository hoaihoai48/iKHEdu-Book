#include <bits/stdc++.h>
using namespace std;

// Cherry Pickup / 2 đường đi đồng thời trên lưới: step = r1 + c1 = r2 + c2
long long dp[205][205][205];
long long grid[205][205];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> grid[i][j];
        }
    }

    memset(dp, -1, sizeof(dp));
    dp[1][1][1] = grid[1][1];

    for (int step = 2; step <= n + m; ++step) {
        for (int r1 = 1; r1 <= n; ++r1) {
            int c1 = step - r1;
            if (c1 < 1 || c1 > m) continue;

            for (int r2 = 1; r2 <= n; ++r2) {
                int c2 = step - r2;
                if (c2 < 1 || c2 > m) continue;

                long long prev_max = -1;
                prev_max = max(prev_max, dp[step - 1][r1 - 1][r2 - 1]);
                prev_max = max(prev_max, dp[step - 1][r1 - 1][r2]);
                prev_max = max(prev_max, dp[step - 1][r1][r2 - 1]);
                prev_max = max(prev_max, dp[step - 1][r1][r2]);

                if (prev_max != -1) {
                    long long gain = (r1 == r2) ? grid[r1][c1] : (grid[r1][c1] + grid[r2][c2]);
                    dp[step][r1][r2] = prev_max + gain;
                }
            }
        }
    }

    cout << max(0LL, dp[n + m][n][n]) << "\n";
    return 0;
}
