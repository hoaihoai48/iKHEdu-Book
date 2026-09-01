#include <bits/stdc++.h>
using namespace std;

// Merge Sort Tree lưu vector đã sắp xếp tại mỗi nút O(N log^2 N)
const int MAXN = 100005;
vector<int> tree_vec[4 * MAXN];
int a[MAXN];

void build(int node, int start, int end) {
    if (start == end) {
        tree_vec[node].push_back(a[start]);
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    merge(tree_vec[2 * node].begin(), tree_vec[2 * node].end(),
          tree_vec[2 * node + 1].begin(), tree_vec[2 * node + 1].end(),
          back_inserter(tree_vec[node]));
}

int query(int node, int start, int end, int l, int r, int k) {
    if (r < start || end < l) return 0;
    if (l <= start && end <= r) {
        return tree_vec[node].end() - upper_bound(tree_vec[node].begin(), tree_vec[node].end(), k);
    }
    int mid = (start + end) / 2;
    return query(2 * node, start, mid, l, r, k) + query(2 * node + 1, mid + 1, end, l, r, k);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= n; ++i) cin >> a[i];
    build(1, 1, n);

    while (q--) {
        int l, r, k;
        cin >> l >> r >> k;
        cout << query(1, 1, n, l, r, k) << "\n";
    }
    return 0;
}
