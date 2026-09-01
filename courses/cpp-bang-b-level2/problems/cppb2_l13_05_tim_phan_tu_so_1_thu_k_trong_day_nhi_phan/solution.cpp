#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<int> tree;
    SegmentTree(int n) : n(n), tree(4 * n, 0) {}

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    int find_kth(int node, int l, int r, int k) {
        if (l == r) return l;
        int mid = l + (r - l) / 2;
        if (tree[2 * node] >= k) return find_kth(2 * node, l, mid, k);
        else return find_kth(2 * node + 1, mid + 1, r, k - tree[2 * node]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    SegmentTree st(n);
    for (int i = 1; i <= n; ++i) {
        int bit; cin >> bit;
        st.update(1, 1, n, i, bit);
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx, val; cin >> idx >> val;
            st.update(1, 1, n, idx, val);
        } else {
            int k; cin >> k;
            cout << st.find_kth(1, 1, n, k) << "\n";
        }
    }
    return 0;
}
