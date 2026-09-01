#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;
    SegmentTree(int n) : n(n), tree(4 * n, 1e18) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    void update(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 1e18;
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return min(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx; long long val; cin >> idx >> val;
            st.update(1, 1, n, idx, val);
        } else {
            int l, r; cin >> l >> r;
            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
