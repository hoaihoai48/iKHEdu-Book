#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> bit;
    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int x, long long val) {
        for (; x <= n; x += x & -x) bit[x] += val;
    }

    long long query(int x) {
        long long sum = 0;
        for (; x > 0; x -= x & -x) sum += bit[x];
        return sum;
    }

    long long queryRange(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    FenwickTree ft(n);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        ft.update(i, x);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            ft.update(pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << ft.queryRange(l, r) << "\n";
        }
    }
    return 0;
}
