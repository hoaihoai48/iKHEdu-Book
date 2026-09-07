#include <bits/stdc++.h>
using namespace std;
string S;
int T;
long long memo[20][200][200];
int vis[20][200][200];
int cur = 1;
long long dfs(int p, int sum, int rem, bool tight) {
    if (sum > T) return 0;
    if (p == (int)S.size()) return (sum == T && rem == 0) ? 1 : 0;
    if (!tight && vis[p][sum][rem] == cur) return memo[p][sum][rem];
    long long r = 0;
    int lim = tight ? S[p] - '0' : 9;
    for (int d = 0; d <= lim; d++)
        r += dfs(p + 1, sum + d, (rem * 10 + d) % T, tight && d == lim);
    if (!tight) { vis[p][sum][rem] = cur; memo[p][sum][rem] = r; }
    return r;
}
long long countLE(long long X) {
    if (X <= 0) return 0;
    S = to_string(X);
    long long ans = 0;
    for (T = 1; T <= 9 * (int)S.size(); T++) { cur++; ans += dfs(0, 0, 0, true); }
    return ans;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long L, R;
    if (!(cin >> L >> R)) return 0;
    cout << countLE(R) - countLE(L - 1) << "\n";
    return 0;
}
