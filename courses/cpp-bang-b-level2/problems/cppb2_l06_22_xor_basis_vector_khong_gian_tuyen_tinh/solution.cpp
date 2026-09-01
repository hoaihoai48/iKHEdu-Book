#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> basis(64, 0);
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        for (int b = 62; b >= 0; --b) {
            if (x & (1LL << b)) {
                if (!basis[b]) { basis[b] = x; break; }
                x ^= basis[b];
            }
        }
    }
    long long ans = 0;
    for (int b = 62; b >= 0; --b) ans = max(ans, ans ^ basis[b]);
    cout << ans << "\n";
    return 0;
}
