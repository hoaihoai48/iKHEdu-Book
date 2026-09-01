#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][11][2][2];

long long solve_dp(int idx, int prev, bool tight, bool leading_zero) {
    if (idx == (int)S_str.size()) return 1;
    if (dp[idx][prev + 1][tight][leading_zero] != -1) return dp[idx][prev + 1][tight][leading_zero];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (!leading_zero && d == prev) continue;
        bool next_lead = leading_zero && (d == 0);
        ans += solve_dp(idx + 1, next_lead ? -1 : d, tight && (d == limit), next_lead);
    }
    return dp[idx][prev + 1][tight][leading_zero] = ans;
}

long long count_lucid(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, -1, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_lucid(R) - count_lucid(L - 1) << "\n";
    return 0;
}
