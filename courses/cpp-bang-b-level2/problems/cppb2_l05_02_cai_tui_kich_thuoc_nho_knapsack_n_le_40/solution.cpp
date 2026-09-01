#include <bits/stdc++.h>
using namespace std;

long long hanoi4(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    vector<long long> dp(n + 1, 1e18);
    dp[0] = 0; dp[1] = 1;
    for (int i = 2; i <= n; ++i) {
        for (int k = 1; k < i; ++k) {
            dp[i] = min(dp[i], 2 * dp[k] + (1LL << (i - k)) - 1);
        }
    }
    return dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k == 3) {
        cout << (1LL << n) - 1 << "\n";
    } else {
        cout << hanoi4(n) << "\n";
    }
    return 0;
}
