#include <bits/stdc++.h>
using namespace std;
int N, Q;
vector<long long> a, st, lz;
vector<char> has;
void build(int p, int l, int r) {
    if (l == r) { st[p] = a[l]; return; }
    int m = (l + r) / 2;
    build(p * 2, l, m); build(p * 2 + 1, m + 1, r);
    st[p] = min(st[p * 2], st[p * 2 + 1]);
}
void apply(int p, long long v) { st[p] = v; lz[p] = v; has[p] = 1; }
void push(int p) { if (has[p]) { apply(p * 2, lz[p]); apply(p * 2 + 1, lz[p]); has[p] = 0; } }
void update(int p, int l, int r, int u, int v, long long val) {
    if (u <= l && r <= v) { apply(p, val); return; }
    push(p);
    int m = (l + r) / 2;
    if (u <= m) update(p * 2, l, m, u, v, val);
    if (v > m) update(p * 2 + 1, m + 1, r, u, v, val);
    st[p] = min(st[p * 2], st[p * 2 + 1]);
}
long long query(int p, int l, int r, int u, int v) {
    if (u <= l && r <= v) return st[p];
    push(p);
    int m = (l + r) / 2;
    long long r0 = (long long)4e18;
    if (u <= m) r0 = min(r0, query(p * 2, l, m, u, v));
    if (v > m) r0 = min(r0, query(p * 2 + 1, m + 1, r, u, v));
    return r0;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> N >> Q)) return 0;
    a.assign(N + 1, 0);
    for (int i = 1; i <= N; i++) cin >> a[i];
    st.assign(4 * N + 4, 0); lz.assign(4 * N + 4, 0); has.assign(4 * N + 4, 0);
    build(1, 1, N);
    while (Q--) {
        int t; cin >> t;
        if (t == 1) { int l, r; long long v; cin >> l >> r >> v; update(1, 1, N, l, r, v); }
        else { int l, r; cin >> l >> r; cout << query(1, 1, N, l, r) << "\n"; }
    }
    return 0;
}
