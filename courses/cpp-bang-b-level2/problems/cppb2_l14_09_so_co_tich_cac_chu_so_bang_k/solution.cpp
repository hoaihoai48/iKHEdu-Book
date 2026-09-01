#include <bits/stdc++.h>
using namespace std;

string S_str;
long long dp[20][50][2][2];

long long solve_dp(int idx, int diff, bool tight, bool lead) {
    if (idx == (int)S_str.size()) return (!lead && diff == 25);
    if (dp[idx][diff][tight][lead] != -1) return dp[idx][diff][tight][lead];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_lead = lead && (d == 0);
        int next_diff = diff + (next_lead ? 0 : (d % 2 == 0 ? 1 : -1));
        ans += solve_dp(idx + 1, next_diff, tight && (d == limit), next_lead);
    }
    return dp[idx][diff][tight][lead] = ans;
}

long long count_balanced(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 25, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_balanced(R) - count_balanced(L - 1) << "\n";
    return 0;
}
