#include <bits/stdc++.h>
using namespace std;
const long long NEG_INF = (long long)-4e18;
int N, Q;
vector<long long> a, sum, mx, se;
vector<int> cnt;
void pull(int p) {
    sum[p] = sum[p * 2] + sum[p * 2 + 1];
    if (mx[p * 2] > mx[p * 2 + 1]) { mx[p] = mx[p * 2]; cnt[p] = cnt[p * 2]; se[p] = max(se[p * 2], mx[p * 2 + 1]); }
    else if (mx[p * 2] < mx[p * 2 + 1]) { mx[p] = mx[p * 2 + 1]; cnt[p] = cnt[p * 2 + 1]; se[p] = max(mx[p * 2], se[p * 2 + 1]); }
    else { mx[p] = mx[p * 2]; cnt[p] = cnt[p * 2] + cnt[p * 2 + 1]; se[p] = max(se[p * 2], se[p * 2 + 1]); }
}
void applyChmin(int p, long long x) {
    if (mx[p] <= x) return;
    sum[p] -= (mx[p] - x) * cnt[p];
    mx[p] = x;
}
void push(int p) {
    applyChmin(p * 2, mx[p]);
    applyChmin(p * 2 + 1, mx[p]);
}
void build(int p, int l, int r) {
    if (l == r) { sum[p] = mx[p] = a[l]; se[p] = NEG_INF; cnt[p] = 1; return; }
    int m = (l + r) / 2;
    build(p * 2, l, m); build(p * 2 + 1, m + 1, r);
    pull(p);
}
void rangeChmin(int p, int l, int r, int u, int v, long long x) {
    if (r < u || l > v || mx[p] <= x) return;
    if (u <= l && r <= v && se[p] < x) { applyChmin(p, x); return; }
    push(p);
    int m = (l + r) / 2;
    rangeChmin(p * 2, l, m, u, v, x);
    rangeChmin(p * 2 + 1, m + 1, r, u, v, x);
    pull(p);
}
long long rangeSum(int p, int l, int r, int u, int v) {
    if (u <= l && r <= v) return sum[p];
    push(p);
    int m = (l + r) / 2;
    long long s = 0;
    if (u <= m) s += rangeSum(p * 2, l, m, u, v);
    if (v > m) s += rangeSum(p * 2 + 1, m + 1, r, u, v);
    return s;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> N >> Q)) return 0;
    a.assign(N + 1, 0);
    for (int i = 1; i <= N; i++) cin >> a[i];
    sum.assign(4 * N + 4, 0); mx.assign(4 * N + 4, 0);
    se.assign(4 * N + 4, NEG_INF); cnt.assign(4 * N + 4, 0);
    build(1, 1, N);
    while (Q--) {
        int t; cin >> t;
        if (t == 1) { int l, r; long long x; cin >> l >> r >> x; rangeChmin(1, 1, N, l, r, x); }
        else { int l, r; cin >> l >> r; cout << rangeSum(1, 1, N, l, r) << "\n"; }
    }
    return 0;
}
