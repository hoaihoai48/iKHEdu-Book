#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> d(n + 2, 0);

    while (q--) {
        int l, r;
        long long v;
        cin >> l >> r >> v;
        d[l] += v;
        d[r + 1] -= v;
    }

    long long current = 0;
    for (int i = 1; i <= n; ++i) {
        current += d[i];
        cout << current << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
