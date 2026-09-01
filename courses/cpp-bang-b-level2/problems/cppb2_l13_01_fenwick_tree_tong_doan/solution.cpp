#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> tree;
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, long long delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }

    long long query_range(int l, int r) {
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    FenwickTree bit(n);
    for (int i = 1; i <= n; ++i) {
        long long x; cin >> x;
        bit.update(i, x);
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx; long long val;
            cin >> idx >> val;
            bit.update(idx, val);
        } else {
            int l, r; cin >> l >> r;
            cout << bit.query_range(l, r) << "\n";
        }
    }
    return 0;
}
