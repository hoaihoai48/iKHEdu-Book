#include <bits/stdc++.h>
using namespace std;

// Fenwick Tree 2D tính tổng hình chữ nhật O(log N * log M)
const int MAXN = 1005;
long long bit2d[MAXN][MAXN];
int N, M;

void update(int r, int c, long long val) {
    for (int i = r; i <= N; i += i & -i) {
        for (int j = c; j <= M; j += j & -j) {
            bit2d[i][j] += val;
        }
    }
}

long long query(int r, int c) {
    long long sum = 0;
    for (int i = r; i > 0; i -= i & -i) {
        for (int j = c; j > 0; j -= j & -j) {
            sum += bit2d[i][j];
        }
    }
    return sum;
}

long long query_rect(int r1, int c1, int r2, int c2) {
    return query(r2, c2) - query(r1 - 1, c2) - query(r2, c1 - 1) + query(r1 - 1, c1 - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> N >> M >> q)) return 0;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int r, c; long long val;
            cin >> r >> c >> val;
            update(r, c, val);
        } else {
            int r1, c1, r2, c2;
            cin >> r1 >> c1 >> r2 >> c2;
            cout << query_rect(r1, c1, r2, c2) << "\n";
        }
    }
    return 0;
}
