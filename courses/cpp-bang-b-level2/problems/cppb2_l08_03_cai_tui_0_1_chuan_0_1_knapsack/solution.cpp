#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<long long> w(n), v(n);
    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];

    vector<long long> dp(W + 1, 0);
    for (int i = 0; i < n; ++i) {
        for (long long j = W; j >= w[i]; --j) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }

    cout << dp[W] << "\n";
    return 0;
}
