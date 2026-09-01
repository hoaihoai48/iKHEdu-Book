#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][2][2];

long long solve_dp(int idx, bool prev4, bool tight) {
    if (idx == (int)S_str.size()) return 1;
    if (dp[idx][prev4][tight] != -1) return dp[idx][prev4][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (prev4 && d == 9) continue;
        ans += solve_dp(idx + 1, d == 4, tight && (d == limit));
    }
    return dp[idx][prev4][tight] = ans;
}

long long count_no_49(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, false, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_no_49(R) - count_no_49(L - 1) << "\n";
    return 0;
}
