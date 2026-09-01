#include <bits/stdc++.h>
using namespace std;

// Digit DP đếm các số đối xứng (Palindromes) trong [L, R]
long long dp[20][20][2];
string S;

long long solve(int l, int r, bool tight) {
    if (l > r) return 1;
    if (dp[l][r][tight] != -1) return dp[l][r][tight];

    int limit = tight ? (S[l] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        ans += solve(l + 1, r - 1, next_tight);
    }

    return dp[l][r][tight] = ans;
}

long long count_pal(long long N) {
    if (N <= 0) return 0;
    S = to_string(N);
    memset(dp, -1, sizeof(dp));
    return solve(0, S.size() - 1, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_pal(R) - count_pal(L - 1) << "\n";
    return 0;
}
