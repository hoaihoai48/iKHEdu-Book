#include <bits/stdc++.h>
using namespace std;

// Chia mảng thành K tập có tổng bằng nhau bằng Bitmask DP
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    int total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    if (total_sum % k != 0) {
        cout << "NO\n";
        return 0;
    }

    int target = total_sum / k;
    vector<int> dp(1 << n, -1);
    dp[0] = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        if (dp[mask] == -1) continue;
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) {
                if (dp[mask] + a[i] <= target) {
                    dp[mask | (1 << i)] = (dp[mask] + a[i]) % target;
                }
            }
        }
    }

    cout << (dp[(1 << n) - 1] == 0 ? "YES\n" : "NO\n");
    return 0;
}
