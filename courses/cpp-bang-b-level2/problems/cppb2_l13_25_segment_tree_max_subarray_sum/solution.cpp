#include <bits/stdc++.h>
using namespace std;

// Segment Tree tìm dãy con có tổng lớn nhất trong đoạn [L, R]
struct Node {
    long long total, pref, suff, max_sub;
};

Node combine(Node L, Node R) {
    Node res;
    res.total = L.total + R.total;
    res.pref = max(L.pref, L.total + R.pref);
    res.suff = max(R.suff, R.total + L.suff);
    res.max_sub = max({L.max_sub, R.max_sub, L.suff + R.pref});
    return res;
}

const int MAXN = 100005;
Node tree_nodes[4 * MAXN];
long long a[MAXN];

void build(int node, int start, int end) {
    if (start == end) {
        tree_nodes[node] = {a[start], a[start], a[start], a[start]};
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    tree_nodes[node] = combine(tree_nodes[2 * node], tree_nodes[2 * node + 1]);
}

void update(int node, int start, int end, int idx, long long val) {
    if (start == end) {
        tree_nodes[node] = {val, val, val, val};
        return;
    }
    int mid = (start + end) / 2;
    if (idx <= mid) update(2 * node, start, mid, idx, val);
    else update(2 * node + 1, mid + 1, end, idx, val);
    tree_nodes[node] = combine(tree_nodes[2 * node], tree_nodes[2 * node + 1]);
}

Node query(int node, int start, int end, int l, int r) {
    if (l <= start && end <= r) return tree_nodes[node];
    int mid = (start + end) / 2;
    if (r <= mid) return query(2 * node, start, mid, l, r);
    if (l > mid) return query(2 * node + 1, mid + 1, end, l, r);
    return combine(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= n; ++i) cin >> a[i];
    build(1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int idx; long long val;
            cin >> idx >> val;
            update(1, 1, n, idx, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query(1, 1, n, l, r).max_sub << "\n";
        }
    }
    return 0;
}
