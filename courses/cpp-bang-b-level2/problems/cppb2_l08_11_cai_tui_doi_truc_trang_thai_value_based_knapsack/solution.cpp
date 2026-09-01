#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<long long> w(n);
    vector<int> v(n);
    int sum_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> v[i];
        sum_v += v[i];
    }

    vector<long long> dp(sum_v + 1, 1e18);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int val = sum_v; val >= v[i]; --val) {
            dp[val] = min(dp[val], dp[val - v[i]] + w[i]);
        }
    }

    int ans = 0;
    for (int val = sum_v; val >= 0; --val) {
        if (dp[val] <= W) {
            ans = val;
            break;
        }
    }

    cout << ans << "\n";
    return 0;
}
