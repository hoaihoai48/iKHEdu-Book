#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int block_sz = sqrt(n) + 1;
    vector<long long> block_sum((n + block_sz - 1) / block_sz, 0);

    for (int i = 0; i < n; ++i) {
        block_sum[i / block_sz] += a[i];
    }

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int idx; long long val; cin >> idx >> val;
            idx--;
            block_sum[idx / block_sz] += (val - a[idx]);
            a[idx] = val;
        } else {
            int l, r; cin >> l >> r;
            l--; r--;
            long long sum = 0;
            int bl = l / block_sz, br = r / block_sz;
            if (bl == br) {
                for (int i = l; i <= r; ++i) sum += a[i];
            } else {
                for (int i = l; i < (bl + 1) * block_sz; ++i) sum += a[i];
                for (int b = bl + 1; b < br; ++b) sum += block_sum[b];
                for (int i = br * block_sz; i <= r; ++i) sum += a[i];
            }
            cout << sum << "\n";
        }
    }
    return 0;
}
