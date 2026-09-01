#include <bits/stdc++.h>
using namespace std;

struct LazySegmentTree {
    int n;
    vector<long long> tree, lazy;
    LazySegmentTree(int n) : n(n), tree(4 * n, 0), lazy(4 * n, 0) {}

    void push(int node, int l, int r) {
        if (lazy[node] != 0) {
            int mid = l + (r - l) / 2;
            tree[2 * node] += lazy[node] * (mid - l + 1);
            lazy[2 * node] += lazy[node];
            tree[2 * node + 1] += lazy[node] * (r - mid);
            lazy[2 * node + 1] += lazy[node];
            lazy[node] = 0;
        }
    }

    void update_range(int node, int l, int r, int ql, int qr, long long val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            tree[node] += val * (r - l + 1);
            lazy[node] += val;
            return;
        }
        push(node, l, r);
        int mid = l + (r - l) / 2;
        update_range(2 * node, l, mid, ql, qr, val);
        update_range(2 * node + 1, mid + 1, r, ql, qr, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    long long query_range(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return tree[node];
        push(node, l, r);
        int mid = l + (r - l) / 2;
        return query_range(2 * node, l, mid, ql, qr) + query_range(2 * node + 1, mid + 1, r, ql, qr);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    LazySegmentTree st(n);
    for (int i = 1; i <= n; ++i) {
        long long x; cin >> x;
        st.update_range(1, 1, n, i, i, x);
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int l, r; long long val; cin >> l >> r >> val;
            st.update_range(1, 1, n, l, r, val);
        } else {
            int l, r; cin >> l >> r;
            cout << st.query_range(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
