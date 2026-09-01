#include <bits/stdc++.h>
using namespace std;

// Segment Tree Beats hỗ trợ gán A[i] = min(A[i], x) trên đoạn
const int MAXN = 100005;
struct Node {
    long long sum;
    long long max1, max2, max_cnt;
} tree[4 * MAXN];

long long a[MAXN];

void push_up(int node) {
    tree[node].sum = tree[2 * node].sum + tree[2 * node + 1].sum;
    if (tree[2 * node].max1 == tree[2 * node + 1].max1) {
        tree[node].max1 = tree[2 * node].max1;
        tree[node].max2 = max(tree[2 * node].max2, tree[2 * node + 1].max2);
        tree[node].max_cnt = tree[2 * node].max_cnt + tree[2 * node + 1].max_cnt;
    } else if (tree[2 * node].max1 > tree[2 * node + 1].max1) {
        tree[node].max1 = tree[2 * node].max1;
        tree[node].max2 = max(tree[2 * node].max2, tree[2 * node + 1].max1);
        tree[node].max_cnt = tree[2 * node].max_cnt;
    } else {
        tree[node].max1 = tree[2 * node + 1].max1;
        tree[node].max2 = max(tree[2 * node].max1, tree[2 * node + 1].max2);
        tree[node].max_cnt = tree[2 * node + 1].max_cnt;
    }
}

void build(int node, int start, int end) {
    if (start == end) {
        tree[node] = {a[start], a[start], -1, 1};
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    push_up(node);
}

void update_min(int node, int start, int end, int l, int r, long long val) {
    if (r < start || end < l || val >= tree[node].max1) return;
    if (l <= start && end <= r && val > tree[node].max2) {
        tree[node].sum -= (tree[node].max1 - val) * tree[node].max_cnt;
        tree[node].max1 = val;
        return;
    }
    int mid = (start + end) / 2;
    update_min(2 * node, start, mid, l, r, val);
    update_min(2 * node + 1, mid + 1, end, l, r, val);
    push_up(node);
}

long long query_sum(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return 0;
    if (l <= start && end <= r) return tree[node].sum;
    int mid = (start + end) / 2;
    return query_sum(2 * node, start, mid, l, r) + query_sum(2 * node + 1, mid + 1, end, l, r);
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
            int l, r; long long val;
            cin >> l >> r >> val;
            update_min(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query_sum(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
