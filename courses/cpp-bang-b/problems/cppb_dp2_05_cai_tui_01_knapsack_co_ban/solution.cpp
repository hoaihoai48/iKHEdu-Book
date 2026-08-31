#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> dp(w + 1, 0);

    for (int i = 0; i < n; ++i) {
        long long weight, val;
        cin >> weight >> val;
        for (int j = w; j >= weight; --j) {
            dp[j] = max(dp[j], dp[j - weight] + val);
        }
    }

    long long ans = 0;
    for (int j = 0; j <= w; ++j) ans = max(ans, dp[j]);
    cout << ans << "\n";
    return 0;
}
