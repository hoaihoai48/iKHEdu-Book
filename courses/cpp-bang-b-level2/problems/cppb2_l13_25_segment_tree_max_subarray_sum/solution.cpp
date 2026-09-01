#include <bits/stdc++.h>
using namespace std;

// Segment Tree Max Subarray Sum dùng 4 mảng song song nguyên bản
const int MAXN = 100005;
long long tree_total[4 * MAXN], tree_pref[4 * MAXN], tree_suff[4 * MAXN], tree_max_sub[4 * MAXN];
long long a[MAXN];

void push_up(int node) {
    int left = 2 * node, right = 2 * node + 1;
    tree_total[node] = tree_total[left] + tree_total[right];
    tree_pref[node] = max(tree_pref[left], tree_total[left] + tree_pref[right]);
    tree_suff[node] = max(tree_suff[right], tree_total[right] + tree_suff[left]);
    tree_max_sub[node] = max({tree_max_sub[left], tree_max_sub[right], tree_suff[left] + tree_pref[right]});
}

void build(int node, int start, int end) {
    if (start == end) {
        tree_total[node] = tree_pref[node] = tree_suff[node] = tree_max_sub[node] = a[start];
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    push_up(node);
}

void update(int node, int start, int end, int idx, long long val) {
    if (start == end) {
        tree_total[node] = tree_pref[node] = tree_suff[node] = tree_max_sub[node] = val;
        return;
    }
    int mid = (start + end) / 2;
    if (idx <= mid) update(2 * node, start, mid, idx, val);
    else update(2 * node + 1, mid + 1, end, idx, val);
    push_up(node);
}

vector<long long> query(int node, int start, int end, int l, int r) {
    if (l <= start && end <= r) {
        return {tree_total[node], tree_pref[node], tree_suff[node], tree_max_sub[node]};
    }
    int mid = (start + end) / 2;
    if (r <= mid) return query(2 * node, start, mid, l, r);
    if (l > mid) return query(2 * node + 1, mid + 1, end, l, r);

    auto L = query(2 * node, start, mid, l, r);
    auto R = query(2 * node + 1, mid + 1, end, l, r);

    long long tot = L[0] + R[0];
    long long pref = max(L[1], L[0] + R[1]);
    long long suff = max(R[2], R[0] + L[2]);
    long long mx = max({L[3], R[3], L[2] + R[1]});
    return {tot, pref, suff, mx};
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
            cout << query(1, 1, n, l, r)[3] << "\n";
        }
    }
    return 0;
}
