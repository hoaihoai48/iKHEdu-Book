#include <bits/stdc++.h>
using namespace std;

struct FenwickTree2D {
    int n, m;
    vector<vector<long long>> tree;
    FenwickTree2D(int n, int m) : n(n), m(m), tree(n + 1, vector<long long>(m + 1, 0)) {}

    void update(int r, int c, long long val) {
        for (int i = r; i <= n; i += i & -i) {
            for (int j = c; j <= m; j += j & -j) {
                tree[i][j] += val;
            }
        }
    }

    long long query(int r, int c) {
        long long sum = 0;
        for (int i = r; i > 0; i -= i & -i) {
            for (int j = c; j > 0; j -= j & -j) {
                sum += tree[i][j];
            }
        }
        return sum;
    }

    long long query_rect(int r1, int c1, int r2, int c2) {
        return query(r2, c2) - query(r1 - 1, c2) - query(r2, c1 - 1) + query(r1 - 1, c1 - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    FenwickTree2D bit(n, m);

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int r, c; long long val; cin >> r >> c >> val;
            bit.update(r, c, val);
        } else {
            int r1, c1, r2, c2; cin >> r1 >> c1 >> r2 >> c2;
            cout << bit.query_rect(r1, c1, r2, c2) << "\n";
        }
    }
    return 0;
}
