#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> bit;
    FenwickTree(int n) : n(n), bit(n + 2, 0) {}

    void update(int x, long long val) {
        for (; x <= n; x += x & -x) bit[x] += val;
    }

    long long query(int x) {
        long long sum = 0;
        for (; x > 0; x -= x & -x) sum += bit[x];
        return sum;
    }

    void updateRange(int l, int r, long long val) {
        update(l, val);
        update(r + 1, -val);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    FenwickTree ft(n);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        ft.updateRange(i, i, a[i]);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Cộng val vào [L, R]
            int l, r;
            long long val;
            cin >> l >> r >> val;
            ft.updateRange(l, r, val);
        } else { // Hỏi giá trị tại pos
            int pos;
            cin >> pos;
            cout << ft.query(pos) << "\n";
        }
    }
    return 0;
}
