#include <bits/stdc++.h>
using namespace std;
string S;
long long memo[20][2][1 << 10];
char vis[20][2][1 << 10];
long long dfs(int p, bool tight, bool started, int mask) {
    if (p == (int)S.size()) return (started && mask == (1 << 10) - 1) ? 1 : 0;
    if (!tight && vis[p][started][mask]) return memo[p][started][mask];
    long long r = 0;
    int lim = tight ? S[p] - '0' : 9;
    for (int d = 0; d <= lim; d++) {
        bool ns = started || d != 0;
        int nm = ns ? (mask | (1 << d)) : 0;
        r += dfs(p + 1, tight && d == lim, ns, nm);
    }
    if (!tight) { vis[p][started][mask] = 1; memo[p][started][mask] = r; }
    return r;
}
long long countLE(long long X) {
    if (X < 0) return 0;
    S = to_string(X);
    memset(vis, 0, sizeof vis);
    return dfs(0, true, false, 0);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long L, R;
    if (!(cin >> L >> R)) return 0;
    cout << countLE(R) - countLE(L - 1) << "\n";
    return 0;
}
