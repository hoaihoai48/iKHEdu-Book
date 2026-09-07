#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long K;
    if (!(cin >> n >> K)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int n1 = n / 2;
    vector<long long> x1, x2;
    x1.reserve(1u << min(n1, 22));
    for (long long mask = 0; mask < (1LL << n1); ++mask) {
        long long xr = 0;
        for (int i = 0; i < n1; ++i) if (mask & (1LL << i)) xr ^= a[i];
        x1.push_back(xr);
    }
    int n2 = n - n1;
    x2.reserve(1u << min(n2, 22));
    for (long long mask = 0; mask < (1LL << n2); ++mask) {
        long long xr = 0;
        for (int i = 0; i < n2; ++i) if (mask & (1LL << i)) xr ^= a[n1 + i];
        x2.push_back(xr);
    }
    sort(x2.begin(), x2.end());

    long long ans = 0;
    for (long long v : x1) {
        auto r = equal_range(x2.begin(), x2.end(), K ^ v);
        ans += (long long)(r.second - r.first);
    }
    cout << ans << "\n";
    return 0;
}
