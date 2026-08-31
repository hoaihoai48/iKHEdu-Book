#include <bits/stdc++.h>
using namespace std;

struct SegmentTreeLazy {
    int n;
    vector<long long> tree, lazy;
    SegmentTreeLazy(int n) : n(n), tree(4 * n + 5, 0), lazy(4 * n + 5, 0) {}

    void push(int id, int l, int r) {
        if (lazy[id] != 0) {
            int mid = (l + r) / 2;
            tree[2 * id] += lazy[id] * (mid - l + 1);
            lazy[2 * id] += lazy[id];
            tree[2 * id + 1] += lazy[id] * (r - mid);
            lazy[2 * id + 1] += lazy[id];
            lazy[id] = 0;
        }
    }

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = tree[2 * id] + tree[2 * id + 1];
    }

    void updateRange(int id, int l, int r, int u, int v, long long val) {
        if (v < l || r < u) return;
        if (u <= l && r <= v) {
            tree[id] += val * (r - l + 1);
            lazy[id] += val;
            return;
        }
        push(id, l, r);
        int mid = (l + r) / 2;
        updateRange(2 * id, l, mid, u, v, val);
        updateRange(2 * id + 1, mid + 1, r, u, v, val);
        tree[id] = tree[2 * id] + tree[2 * id + 1];
    }

    long long query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return 0;
        if (u <= l && r <= v) return tree[id];
        push(id, l, r);
        int mid = (l + r) / 2;
        return query(2 * id, l, mid, u, v) + query(2 * id + 1, mid + 1, r, u, v);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTreeLazy st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long val;
            cin >> l >> r >> val;
            st.updateRange(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
