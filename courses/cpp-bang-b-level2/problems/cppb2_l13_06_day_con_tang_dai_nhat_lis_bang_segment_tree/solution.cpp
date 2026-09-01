#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<int> tree;
    SegmentTree(int n) : n(n), tree(4 * n, 0) {}

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = max(tree[node], val);
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l || ql > qr) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    SegmentTree st(vals.size());
    int max_lis = 0;

    for (int i = 0; i < n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        int best_prev = st.query(1, 1, vals.size(), 1, rank - 1);
        int cur_len = best_prev + 1;
        max_lis = max(max_lis, cur_len);
        st.update(1, 1, vals.size(), rank, cur_len);
    }

    cout << max_lis << "\n";
    return 0;
}
