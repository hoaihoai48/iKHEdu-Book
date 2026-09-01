#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][1 << 10][2][2];

long long solve_dp(int idx, int mask, bool tight, bool lead) {
    if (idx == (int)S_str.size()) return !lead;
    if (dp[idx][mask][tight][lead] != -1) return dp[idx][mask][tight][lead];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (!lead && ((mask >> d) & 1)) continue;
        bool next_lead = lead && (d == 0);
        int next_mask = next_lead ? 0 : (mask | (1 << d));
        ans += solve_dp(idx + 1, next_mask, tight && (d == limit), next_lead);
    }
    return dp[idx][mask][tight][lead] = ans;
}

long long count_distinct(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 0, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_distinct(R) - count_distinct(L - 1) << "\n";
    return 0;
}
