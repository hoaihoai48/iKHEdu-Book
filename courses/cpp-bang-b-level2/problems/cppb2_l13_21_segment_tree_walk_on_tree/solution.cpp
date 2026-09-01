#include <bits/stdc++.h>
using namespace std;

// Walk on Segment Tree tìm vị trí đầu tiên >= X trong O(log N)
const int MAXN = 200005;
long long tree_max[4 * MAXN], a[MAXN];

void build(int node, int start, int end) {
    if (start == end) {
        tree_max[node] = a[start];
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    tree_max[node] = max(tree_max[2 * node], tree_max[2 * node + 1]);
}

int walk(int node, int start, int end, int l, int r, long long x) {
    if (r < start || end < l || tree_max[node] < x) return -1;
    if (start == end) return start;

    int mid = (start + end) / 2;
    int res = walk(2 * node, start, mid, l, r, x);
    if (res != -1) return res;
    return walk(2 * node + 1, mid + 1, end, l, r, x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= n; ++i) cin >> a[i];
    build(1, 1, n);

    while (q--) {
        int l, r; long long x;
        cin >> l >> r >> x;
        cout << walk(1, 1, n, l, r, x) << "\n";
    }
    return 0;
}
