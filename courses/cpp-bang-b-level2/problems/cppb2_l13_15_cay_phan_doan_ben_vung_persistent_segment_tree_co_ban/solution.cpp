#include <bits/stdc++.h>
using namespace std;

struct MergeSortTree {
    int n;
    vector<vector<long long>> tree;
    MergeSortTree(int n) : n(n), tree(4 * n) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            tree[node] = {a[l]};
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node].resize(tree[2 * node].size() + tree[2 * node + 1].size());
        merge(tree[2 * node].begin(), tree[2 * node].end(),
              tree[2 * node + 1].begin(), tree[2 * node + 1].end(),
              tree[node].begin());
    }

    int query(int node, int l, int r, int ql, int qr, long long k) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) {
            return lower_bound(tree[node].begin(), tree[node].end(), k) - tree[node].begin();
        }
        int mid = l + (r - l) / 2;
        return query(2 * node, l, mid, ql, qr, k) + query(2 * node + 1, mid + 1, r, ql, qr, k);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    MergeSortTree mst(n);
    mst.build(a, 1, 1, n);

    while (q--) {
        int l, r; long long k;
        cin >> l >> r >> k;
        cout << mst.query(1, 1, n, l, r, k) << "\n";
    }
    return 0;
}
