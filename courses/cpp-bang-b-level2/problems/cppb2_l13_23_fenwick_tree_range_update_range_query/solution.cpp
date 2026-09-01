#include <bits/stdc++.h>
using namespace std;

// Cây Fenwick hỗ trợ cập nhật đoạn và truy vấn tổng đoạn bằng 2 cây BIT
const int MAXN = 200005;
long long B1[MAXN], B2[MAXN];
int N;

void add(long long* b, int idx, long long val) {
    for (; idx <= N; idx += idx & -idx) b[idx] += val;
}

void range_add(int l, int r, long long val) {
    add(B1, l, val);
    add(B1, r + 1, -val);
    add(B2, l, val * (l - 1));
    add(B2, r + 1, -val * r);
}

long long prefix_sum(long long* b, int idx) {
    long long sum = 0;
    for (; idx > 0; idx -= idx & -idx) sum += b[idx];
    return sum;
}

long long query_prefix(int idx) {
    return prefix_sum(B1, idx) * idx - prefix_sum(B2, idx);
}

long long range_query(int l, int r) {
    return query_prefix(r) - query_prefix(l - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> N >> q)) return 0;

    for (int i = 1; i <= N; ++i) {
        long long x; cin >> x;
        range_add(i, i, x);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r; long long val;
            cin >> l >> r >> val;
            range_add(l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << range_query(l, r) << "\n";
        }
    }
    return 0;
}
