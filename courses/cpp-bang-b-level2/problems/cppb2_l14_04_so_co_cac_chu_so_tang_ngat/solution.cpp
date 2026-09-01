#include <bits/stdc++.h>
using namespace std;

// Digit DP đếm số lượng số có các chữ số tăng ngặt trong [L, R]
long long dp[20][11][2][2];
string S;

long long solve(int idx, int last_digit, bool tight, bool leading_zero) {
    if (idx == (int)S.size()) {
        return !leading_zero ? 1 : 0;
    }
    if (dp[idx][last_digit][tight][leading_zero] != -1) {
        return dp[idx][last_digit][tight][leading_zero];
    }

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        if (leading_zero) {
            if (d == 0) {
                ans += solve(idx + 1, 0, next_tight, true);
            } else {
                ans += solve(idx + 1, d, next_tight, false);
            }
        } else {
            if (d > last_digit) {
                ans += solve(idx + 1, d, next_tight, false);
            }
        }
    }

    return dp[idx][last_digit][tight][leading_zero] = ans;
}

long long count_strictly_increasing(long long N) {
    if (N <= 0) return 0;
    S = to_string(N);
    memset(dp, -1, sizeof(dp));
    return solve(0, 0, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_strictly_increasing(R) - count_strictly_increasing(L - 1) << "\n";
    return 0;
}
