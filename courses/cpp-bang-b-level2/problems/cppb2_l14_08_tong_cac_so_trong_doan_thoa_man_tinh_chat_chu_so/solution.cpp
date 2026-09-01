#include <bits/stdc++.h>
using namespace std;

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; ++i) if (n % i == 0) return false;
    return true;
}

string S_str;
long long dp[20][200][2];

long long solve_dp(int idx, int sum, bool tight) {
    if (idx == (int)S_str.size()) return is_prime(sum);
    if (dp[idx][sum][tight] != -1) return dp[idx][sum][tight];

    int limit = tight ? (S_str[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        ans += solve_dp(idx + 1, sum + d, tight && (d == limit));
    }
    return dp[idx][sum][tight] = ans;
}

long long count_prime_sum(long long n) {
    if (n < 0) return 0;
    S_str = to_string(n);
    memset(dp, -1, sizeof(dp));
    return solve_dp(0, 0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_prime_sum(R) - count_prime_sum(L - 1) << "\n";
    return 0;
}
