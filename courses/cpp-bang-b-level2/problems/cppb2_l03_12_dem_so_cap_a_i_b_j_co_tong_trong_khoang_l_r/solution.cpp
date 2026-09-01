#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long L, R;
    if (!(cin >> n >> m >> L >> R)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    sort(b.begin(), b.end());

    long long count = 0;
    for (int i = 0; i < n; ++i) {
        auto it1 = lower_bound(b.begin(), b.end(), L - a[i]);
        auto it2 = upper_bound(b.begin(), b.end(), R - a[i]);
        count += (it2 - it1);
    }

    cout << count << "\n";
    return 0;
}
