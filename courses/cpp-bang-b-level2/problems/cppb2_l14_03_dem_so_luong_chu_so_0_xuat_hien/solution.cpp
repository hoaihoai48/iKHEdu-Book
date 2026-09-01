#include <bits/stdc++.h>
using namespace std;

string S_str;
int forbidden;
long long dp[20][2];

long long solve_dp(int idx, bool tight) {
    if (idx == (int)S_str.size()) return 1;
    if (dp[idx][tight] != -1) return dp[idx][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        if (d == forbidden) continue;
        ans += solve_dp(idx + 1, tight && (d == limit));
    }
    return dp[idx][tight] = ans;
}

long long count_valid(long long n, int d) {
    if (n < 0) return 0;
    S_str = to_string(n);
    forbidden = d;
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int d;
    if (!(cin >> L >> R >> d)) return 0;

    cout << count_valid(R, d) - count_valid(L - 1, d) << "\n";
    return 0;
}
