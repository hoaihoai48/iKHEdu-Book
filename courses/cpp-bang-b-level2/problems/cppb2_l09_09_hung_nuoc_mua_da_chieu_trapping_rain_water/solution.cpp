#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];
    int l = 0, r = n - 1;
    long long lmax = 0, rmax = 0, ans = 0;
    while (l <= r) {
        if (h[l] <= h[r]) {
            if (h[l] >= lmax) lmax = h[l];
            else ans += lmax - h[l];
            ++l;
        } else {
            if (h[r] >= rmax) rmax = h[r];
            else ans += rmax - h[r];
            --r;
        }
    }
    cout << ans << "\n";
    return 0;
}
