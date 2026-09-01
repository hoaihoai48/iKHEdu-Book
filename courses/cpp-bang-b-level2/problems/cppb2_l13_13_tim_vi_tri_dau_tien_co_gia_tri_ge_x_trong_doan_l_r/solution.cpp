#include <bits/stdc++.h>
using namespace std;

struct SegmentTreeBeats {
    int n;
    vector<long long> sum_tree, max_tree;
    SegmentTreeBeats(int n) : n(n), sum_tree(4 * n, 0), max_tree(4 * n, 0) {}

    void build(const vector<long long> &a, int node, int l, int r) {
        if (l == r) {
            sum_tree[node] = max_tree[node] = a[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        sum_tree[node] = sum_tree[2 * node] + sum_tree[2 * node + 1];
        max_tree[node] = max(max_tree[2 * node], max_tree[2 * node + 1]);
    }

    long long query_sum(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return sum_tree[node];
        int mid = l + (r - l) / 2;
        return query_sum(2 * node, l, mid, ql, qr) + query_sum(2 * node + 1, mid + 1, r, ql, qr);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTreeBeats stb(n);
    stb.build(a, 1, 1, n);

    while (q--) {
        int l, r; cin >> l >> r;
        cout << stb.query_sum(1, 1, n, l, r) << "\n";
    }
    return 0;
}
