#include <bits/stdc++.h>
using namespace std;

// Persistent Segment Tree dùng mảng song song nguyên bản
const int MAXN = 200005;
int node_count_val[MAXN * 40];
int node_left_child[MAXN * 40];
int node_right_child[MAXN * 40];
int roots[MAXN], total_nodes;

int update_tree(int prev_root, int start, int end, int val) {
    int cur = ++total_nodes;
    node_count_val[cur] = node_count_val[prev_root] + 1;
    node_left_child[cur] = node_left_child[prev_root];
    node_right_child[cur] = node_right_child[prev_root];

    if (start == end) return cur;

    int mid = (start + end) / 2;
    if (val <= mid) {
        node_left_child[cur] = update_tree(node_left_child[prev_root], start, mid, val);
    } else {
        node_right_child[cur] = update_tree(node_right_child[prev_root], mid + 1, end, val);
    }
    return cur;
}

int query_tree(int node_l, int node_r, int start, int end, int k) {
    if (start == end) return start;
    int count_left = node_count_val[node_left_child[node_r]] - node_count_val[node_left_child[node_l]];
    int mid = (start + end) / 2;
    if (k <= count_left) {
        return query_tree(node_left_child[node_l], node_left_child[node_r], start, mid, k);
    } else {
        return query_tree(node_right_child[node_l], node_right_child[node_r], mid + 1, end, k - count_left);
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
        roots[i] = update_tree(roots[i - 1], 1, m, idx);
    }

    while (q--) {
        int l, r, k;
        cin >> l >> r >> k;
        int ans_idx = query_tree(roots[l - 1], roots[r], 1, m, k);
        cout << vals[ans_idx - 1] << "\n";
    }
    return 0;
}
