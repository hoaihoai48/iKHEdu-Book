#include <bits/stdc++.h>
using namespace std;
string S;
long long K;
map<tuple<int,int,long long>, long long> memo;
long long dfs(int p, bool tight, bool started, long long prod) {
    if (prod > K || (prod > 0 && K % prod != 0)) return 0;
    if (p == (int)S.size()) return (started && prod == K) ? 1 : 0;
    if (!tight) {
        auto key = make_tuple(p, started, prod);
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;
        long long r = 0;
        for (int d = 0; d <= 9; d++) {
            if (!started && d == 0) r += dfs(p + 1, false, false, 0);
            else {
                long long np = started ? prod * d : d;
                r += dfs(p + 1, false, true, np);
            }
        }
        memo[key] = r;
        return r;
    }
    long long r = 0;
    int lim = S[p] - '0';
    for (int d = 0; d <= lim; d++) {
        bool nt = (d == lim);
        if (!started && d == 0) r += dfs(p + 1, nt, false, 0);
        else {
            long long np = started ? prod * d : d;
            r += dfs(p + 1, nt, true, np);
        }
    }
    return r;
}
long long countNoZero(long long X); // fwd
string T2;
long long memo2[20][2];
char vis2[20][2];
long long dfs2(int p, bool tight, bool started) {
    if (p == (int)T2.size()) return started ? 1 : 0;
    if (!tight && vis2[p][started]) return memo2[p][started];
    long long r = 0;
    int lim = tight ? T2[p] - '0' : 9;
    for (int d = 0; d <= lim; d++) {
        if (started && d == 0) continue;
        r += dfs2(p + 1, tight && d == lim, started || d != 0);
    }
    if (!tight) { vis2[p][started] = 1; memo2[p][started] = r; }
    return r;
}
long long countNoZero(long long X) {
    if (X <= 0) return 0;
    T2 = to_string(X);
    memset(vis2, 0, sizeof vis2);
    return dfs2(0, true, false);
}
long long countLE(long long X, long long k) {
    if (X <= 0) return 0;
    K = k;
    if (K == 0) return X - countNoZero(X); // includes 0 itself when range covers it
    if (K == 1) {
        // numbers composed only of digit 1: 1, 11, 111, ...
        long long c = 0, v = 1;
        while (v <= X) { c++; if (v > X / 10) break; v = v * 10 + 1; }
        return c;
    }
    S = to_string(X);
    memo.clear();
    return dfs(0, true, false, 0);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long L, R, k;
    if (!(cin >> L >> R >> k)) return 0;
    cout << countLE(R, k) - countLE(L - 1, k) << "\n";
    return 0;
}
