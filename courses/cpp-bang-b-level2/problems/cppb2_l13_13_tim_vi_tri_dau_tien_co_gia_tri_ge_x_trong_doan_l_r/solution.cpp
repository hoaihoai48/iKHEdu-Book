#include <bits/stdc++.h>
using namespace std;
int N, Q;
vector<long long> a, st;
void build(int p, int l, int r) {
    if (l == r) { st[p] = a[l]; return; }
    int m = (l + r) / 2;
    build(p * 2, l, m); build(p * 2 + 1, m + 1, r);
    st[p] = max(st[p * 2], st[p * 2 + 1]);
}
int findFirst(int p, int l, int r, int u, int v, long long x) {
    if (r < u || l > v || st[p] < x) return -1;
    if (l == r) return l;
    int m = (l + r) / 2;
    int left = findFirst(p * 2, l, m, u, v, x);
    if (left != -1) return left;
    return findFirst(p * 2 + 1, m + 1, r, u, v, x);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> N >> Q)) return 0;
    a.assign(N + 1, 0);
    for (int i = 1; i <= N; i++) cin >> a[i];
    st.assign(4 * N + 4, 0);
    build(1, 1, N);
    while (Q--) {
        int l, r; long long x; cin >> l >> r >> x;
        cout << findFirst(1, 1, N, l, r, x) << "\n";
    }
    return 0;
}
