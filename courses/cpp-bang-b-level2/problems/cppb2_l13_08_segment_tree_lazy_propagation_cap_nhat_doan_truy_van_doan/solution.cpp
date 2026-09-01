#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum, pref, suff, max_sub;
    Node(long long val = 0) {
        sum = val;
        pref = suff = max_sub = val;
    }
};

Node merge_nodes(const Node &L, const Node &R) {
    Node res;
    res.sum = L.sum + R.sum;
    res.pref = max(L.pref, L.sum + R.pref);
    res.suff = max(R.suff, R.sum + L.suff);
    res.max_sub = max({L.max_sub, R.max_sub, L.suff + R.pref});
    return res;
}

struct SegmentTree {
    int n;
    vector<Node> tree;
    SegmentTree(int n) : n(n), tree(4 * n) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            tree[node] = Node(a[l]);
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node] = merge_nodes(tree[2 * node], tree[2 * node + 1]);
    }

    Node query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        if (qr <= mid) return query(2 * node, l, mid, ql, qr);
        if (ql > mid) return query(2 * node + 1, mid + 1, r, ql, qr);
        return merge_nodes(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
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
        int l, r; cin >> l >> r;
        cout << st.query(1, 1, n, l, r).max_sub << "\n";
    }
    return 0;
}
