#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n; int k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> p(k);
    for (int i = 0; i < k; ++i) cin >> p[i];
    long long ans = 0;
    for (int mask = 1; mask < (1 << k); ++mask) {
        long long prod = 1; int cnt = 0;
        for (int i = 0; i < k; ++i) {
            if (mask & (1 << i)) {
                prod *= p[i];
                cnt++;
            }
        }
        if (cnt % 2 == 1) ans += n / prod;
        else ans -= n / prod;
    }
    cout << n - ans << "\n";
    return 0;
}
