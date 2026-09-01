#include <bits/stdc++.h>
using namespace std;

// Persistent Segment Tree tìm phần tử thứ K nhỏ nhất trong đoạn [L, R]
const int MAXN = 200005;
struct Node {
    int count;
    int left, right;
} tree_nodes[MAXN * 40];

int roots[MAXN], node_cnt;

int update(int prev_root, int start, int end, int val) {
    int cur = ++node_cnt;
    tree_nodes[cur] = tree_nodes[prev_root];
    tree_nodes[cur].count++;
    if (start == end) return cur;

    int mid = (start + end) / 2;
    if (val <= mid) {
        tree_nodes[cur].left = update(tree_nodes[prev_root].left, start, mid, val);
    } else {
        tree_nodes[cur].right = update(tree_nodes[prev_root].right, mid + 1, end, val);
    }
    return cur;
}

int query(int node_l, int node_r, int start, int end, int k) {
    if (start == end) return start;
    int count_left = tree_nodes[tree_nodes[node_r].left].count - tree_nodes[tree_nodes[node_l].left].count;
    int mid = (start + end) / 2;
    if (k <= count_left) {
        return query(tree_nodes[node_l].left, tree_nodes[node_r].left, start, mid, k);
    } else {
        return query(tree_nodes[node_l].right, tree_nodes[node_r].right, mid + 1, end, k - count_left);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n + 1), vals;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    roots[0] = 0;
    int m = vals.size();
    for (int i = 1; i <= n; ++i) {
        int idx = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        roots[i] = update(roots[i - 1], 1, m, idx);
    }

    while (q--) {
        int l, r, k;
        cin >> l >> r >> k;
        int ans_idx = query(roots[l - 1], roots[r], 1, m, k);
        cout << vals[ans_idx - 1] << "\n";
    }
    return 0;
}
