#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> d2(n + 3, 0);

    while (q--) {
        long long l, r, s, d;
        cin >> l >> r >> s >> d;
        d2[l] += s;
        d2[l + 1] += (d - s);
        d2[r + 1] -= (s + (r - l + 1) * d);
        d2[r + 2] += (s + (r - l) * d);
    }

    // Lần 1: Khôi phục mảng hiệu bậc 1
    vector<long long> d1(n + 2, 0);
    for (int i = 1; i <= n + 1; ++i) {
        d1[i] = d1[i - 1] + d2[i];
    }

    // Lần 2: Khôi phục mảng giá trị gốc
    vector<long long> a(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        a[i] = a[i - 1] + d1[i];
        cout << a[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
