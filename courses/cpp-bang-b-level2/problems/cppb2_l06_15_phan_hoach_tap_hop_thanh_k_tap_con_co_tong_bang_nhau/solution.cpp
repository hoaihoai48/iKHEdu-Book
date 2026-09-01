#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }

    if (total % k != 0) {
        cout << "NO\n";
        return 0;
    }

    long long target = total / k;
    vector<int> dp(1 << n, -1);
    dp[0] = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        if (dp[mask] == -1) continue;
        for (int i = 0; i < n; ++i) {
            if (!((mask >> i) & 1) && dp[mask] + a[i] <= target) {
                dp[mask | (1 << i)] = (dp[mask] + a[i]) % target;
            }
        }
    }

    cout << (dp[(1 << n) - 1] == 0 ? "YES" : "NO") << "\n";
    return 0;
}
