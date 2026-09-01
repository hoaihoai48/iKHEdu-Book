#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    while (q--) {
        long long l, r;
        cin >> l >> r;
        auto it1 = lower_bound(a.begin(), a.end(), l);
        auto it2 = upper_bound(a.begin(), a.end(), r);
        cout << (it2 - it1) << "\n";
    }
    return 0;
}
