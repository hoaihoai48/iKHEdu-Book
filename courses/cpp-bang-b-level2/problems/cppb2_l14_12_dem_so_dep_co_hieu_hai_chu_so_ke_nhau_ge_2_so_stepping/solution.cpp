#include <bits/stdc++.h>
using namespace std;
string S;
long long memo[20][11];
char vis[20][11];
long long dfs(int p, bool tight, bool started, int prev) {
    if (p == (int)S.size()) return 1;
    if (!tight && vis[p][prev + 1]) return memo[p][prev + 1];
    long long r = 0;
    int lim = tight ? S[p] - '0' : 9;
    for (int d = 0; d <= lim; d++) {
        if (!started && d == 0) r += dfs(p + 1, tight && d == lim, false, -1);
        else if (!started) r += dfs(p + 1, tight && d == lim, true, d);
        else if (abs(d - prev) >= 2) r += dfs(p + 1, tight && d == lim, true, d);
    }
    if (!tight) { vis[p][prev + 1] = 1; memo[p][prev + 1] = r; }
    return r;
}
long long countLE(long long X) {
    if (X < 0) return 0;
    S = to_string(X);
    memset(vis, 0, sizeof vis);
    return dfs(0, true, false, -1);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long L, R;
    if (!(cin >> L >> R)) return 0;
    cout << countLE(R) - countLE(L - 1) << "\n";
    return 0;
}
