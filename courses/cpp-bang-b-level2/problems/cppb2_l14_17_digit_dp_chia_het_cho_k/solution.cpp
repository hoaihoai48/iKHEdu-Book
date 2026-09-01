#include <bits/stdc++.h>
using namespace std;

long long dp[20][100][2][2];
string S;
int K;

long long solve(int idx, int rem, bool tight, bool leading_zero) {
    if (idx == (int)S.size()) {
        return (rem == 0 && !leading_zero) ? 1 : 0;
    }
    if (dp[idx][rem][tight][leading_zero] != -1) {
        return dp[idx][rem][tight][leading_zero];
    }

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        bool next_lz = leading_zero && (d == 0);
        int next_rem = next_lz ? 0 : (rem * 10 + d) % K;
        ans += solve(idx + 1, next_rem, next_tight, next_lz);
    }

    return dp[idx][rem][tight][leading_zero] = ans;
}

long long count_div(long long N, int k) {
    if (N <= 0) return 0;
    S = to_string(N);
    K = k;
    memset(dp, -1, sizeof(dp));
    return solve(0, 0, true, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    int k;
    if (!(cin >> L >> R >> k)) return 0;

    cout << count_div(R, k) - count_div(L - 1, k) << "\n";
    return 0;
}
