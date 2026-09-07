#include <bits/stdc++.h>
using namespace std;
struct Node { long long sum, pref, suff, best; };
const long long NEG = (long long)-4e18;
Node mergeNode(const Node &L, const Node &R) {
    Node r;
    r.sum = L.sum + R.sum;
    r.pref = max(L.pref, L.sum + R.pref);
    r.suff = max(R.suff, R.sum + L.suff);
    r.best = max({L.best, R.best, L.suff + R.pref});
    return r;
}
int N, Q;
vector<long long> a;
vector<Node> st;
void build(int p, int l, int r) {
    if (l == r) { st[p] = {a[l], a[l], a[l], a[l]}; return; }
    int m = (l + r) / 2;
    build(p * 2, l, m); build(p * 2 + 1, m + 1, r);
    st[p] = mergeNode(st[p * 2], st[p * 2 + 1]);
}
Node query(int p, int l, int r, int u, int v) {
    if (u <= l && r <= v) return st[p];
    int m = (l + r) / 2;
    if (v <= m) return query(p * 2, l, m, u, v);
    if (u > m) return query(p * 2 + 1, m + 1, r, u, v);
    return mergeNode(query(p * 2, l, m, u, v), query(p * 2 + 1, m + 1, r, u, v));
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> N >> Q)) return 0;
    a.assign(N + 1, 0);
    for (int i = 1; i <= N; i++) cin >> a[i];
    st.assign(4 * N + 4, {});
    build(1, 1, N);
    while (Q--) {
        int l, r; cin >> l >> r;
        cout << query(1, 1, N, l, r).best << "\n";
    }
    return 0;
}
