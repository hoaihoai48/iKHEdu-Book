#include <bits/stdc++.h>
using namespace std;

// Digit DP đếm các số không chứa chữ số cấm D
long long dp[20][2][2];
string S;
int banned_digit;

long long solve(int idx, bool tight, bool leading_zero) {
    if (idx == (int)S.size()) {
        return !leading_zero ? 1 : 0;
    }
    if (dp[idx][tight][leading_zero] != -1) {
        return dp[idx][tight][leading_zero];
    }

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (!leading_zero && d == banned_digit) continue;
        if (leading_zero && d == banned_digit && d != 0) continue;

        bool next_tight = tight && (d == limit);
        bool next_lz = leading_zero && (d == 0);
        ans += solve(idx + 1, next_tight, next_lz);
    }

    return dp[idx][tight][leading_zero] = ans;
}

long long count_valid(long long N, int b) {
    if (N <= 0) return 0;
    S = to_string(N);
    banned_digit = b;
    memset(dp, -1, sizeof(dp));
    return solve(0, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    int b;
    if (!(cin >> L >> R >> b)) return 0;

    cout << count_valid(R, b) - count_valid(L - 1, b) << "\n";
    return 0;
}
