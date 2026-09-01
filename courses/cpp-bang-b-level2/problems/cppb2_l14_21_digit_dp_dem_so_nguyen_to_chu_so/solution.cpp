#include <bits/stdc++.h>
using namespace std;

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

long long dp[20][200][2][2];
string S;

long long solve(int idx, int sum, bool tight, bool leading_zero) {
    if (idx == (int)S.size()) {
        return (!leading_zero && is_prime(sum)) ? 1 : 0;
    }
    if (dp[idx][sum][tight][leading_zero] != -1) return dp[idx][sum][tight][leading_zero];

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        bool next_lz = leading_zero && (d == 0);
        ans += solve(idx + 1, sum + d, next_tight, next_lz);
    }
    return dp[idx][sum][tight][leading_zero] = ans;
}

long long calc(long long N) {
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

    cout << calc(R) - calc(L - 1) << "\n";
    return 0;
}
