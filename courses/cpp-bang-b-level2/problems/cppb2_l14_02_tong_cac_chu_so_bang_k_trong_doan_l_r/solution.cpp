#include <bits/stdc++.h>
using namespace std;

string S_str;
int target_sum;
long long dp[20][200][2];

long long solve_dp(int idx, int sum, bool tight) {
    if (idx == (int)S_str.size()) return sum == target_sum;
    if (dp[idx][sum][tight] != -1) return dp[idx][sum][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        ans += solve_dp(idx + 1, sum + d, tight && (d == limit));
    }
    return dp[idx][sum][tight] = ans;
}

long long count_sum(long long n, int s) {
    if (n < 0) return 0;
    S_str = to_string(n);
    target_sum = s;
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int s;
    if (!(cin >> L >> R >> s)) return 0;

    cout << count_sum(R, s) - count_sum(L - 1, s) << "\n";
    return 0;
}
