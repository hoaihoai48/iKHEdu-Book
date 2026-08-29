#include <bits/stdc++.h>
using namespace std;

long long count_le(long long x, const vector<long long>& a, const vector<long long>& b) {
    auto it1 = upper_bound(a.begin(), a.end(), x);
    auto it2 = upper_bound(b.begin(), b.end(), x);
    return (it1 - a.begin()) + (it2 - b.begin());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    long long low = -2e9, high = 2e9, ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_le(mid, a, b) >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
