#include <bits/stdc++.h>
using namespace std;

// Digit DP tính tổng bình phương chữ số của tất cả các số trong [L, R]
long long dp[20][2000][2];
string S;

long long solve(int idx, int sum_sq, bool tight) {
    if (idx == (int)S.size()) return sum_sq;
    if (dp[idx][sum_sq][tight] != -1) return dp[idx][sum_sq][tight];

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        ans += solve(idx + 1, sum_sq + d * d, tight && (d == limit));
    }
    return dp[idx][sum_sq][tight] = ans;
}

long long calc(long long N) {
    if (N <= 0) return 0;
    S = to_string(N);
    memset(dp, -1, sizeof(dp));
    return solve(0, 0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << calc(R) - calc(L - 1) << "\n";
    return 0;
}
