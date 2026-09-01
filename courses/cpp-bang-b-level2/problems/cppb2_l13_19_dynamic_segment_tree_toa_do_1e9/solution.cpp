#include <bits/stdc++.h>
using namespace std;

// Cây phân đoạn động cấp phát con trỏ trên miền [1, 10^9]
struct DynamicSegTree {
    struct Node {
        long long sum = 0;
        int left = -1, right = -1;
    };
    vector<Node> tree;

    DynamicSegTree() { tree.emplace_back(); }

    void update(int node, long long start, long long end, long long idx, long long val) {
        tree[node].sum += val;
        if (start == end) return;

        long long mid = start + (end - start) / 2;
        if (idx <= mid) {
            if (tree[node].left == -1) {
                tree[node].left = tree.size();
                tree.emplace_back();
            }
            update(tree[node].left, start, mid, idx, val);
        } else {
            if (tree[node].right == -1) {
                tree[node].right = tree.size();
                tree.emplace_back();
            }
            update(tree[node].right, mid + 1, end, idx, val);
        }
    }

    long long query(int node, long long start, long long end, long long l, long long r) {
        if (node == -1 || r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node].sum;
        long long mid = start + (end - start) / 2;
        return query(tree[node].left, start, mid, l, r) + query(tree[node].right, mid + 1, end, l, r);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    DynamicSegTree seg;
    const long long MAX_COORD = 1000000000;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            long long idx, val;
            cin >> idx >> val;
            seg.update(0, 1, MAX_COORD, idx, val);
        } else {
            long long l, r;
            cin >> l >> r;
            cout << seg.query(0, 1, MAX_COORD, l, r) << "\n";
        }
    }
    return 0;
}
