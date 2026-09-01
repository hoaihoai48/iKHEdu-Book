#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
long long tree_sum[4 * MAXN], lazy[4 * MAXN], a[MAXN];

void build(int node, int start, int end) {
    if (start == end) {
        tree_sum[node] = a[start];
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    tree_sum[node] = tree_sum[2 * node] + tree_sum[2 * node + 1];
}

void push(int node, int start, int end) {
    if (lazy[node] != 0) {
        int mid = (start + end) / 2;
        tree_sum[2 * node] += lazy[node] * (mid - start + 1);
        lazy[2 * node] += lazy[node];
        tree_sum[2 * node + 1] += lazy[node] * (end - mid);
        lazy[2 * node + 1] += lazy[node];
        lazy[node] = 0;
    }
}

void update_range(int node, int start, int end, int l, int r, long long val) {
    if (r < start || end < l) return;
    if (l <= start && end <= r) {
        tree_sum[node] += val * (end - start + 1);
        lazy[node] += val;
        return;
    }
    push(node, start, end);
    int mid = (start + end) / 2;
    update_range(2 * node, start, mid, l, r, val);
    update_range(2 * node + 1, mid + 1, end, l, r, val);
    tree_sum[node] = tree_sum[2 * node] + tree_sum[2 * node + 1];
}

long long query_range(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return 0;
    if (l <= start && end <= r) return tree_sum[node];
    push(node, start, end);
    int mid = (start + end) / 2;
    return query_range(2 * node, start, mid, l, r) + query_range(2 * node + 1, mid + 1, end, l, r);
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
            update_range(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query_range(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
