#include <bits/stdc++.h>
using namespace std;

// Đổi trục DP: dp[v] là trọng lượng nhỏ nhất để đạt được tổng giá trị v
const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<long long> w(n), v(n);
    int max_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> v[i];
        max_v += v[i];
    }

    vector<long long> dp(max_v + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int val = max_v; val >= v[i]; --val) {
            if (dp[val - v[i]] != INF) {
                dp[val] = min(dp[val], dp[val - v[i]] + w[i]);
            }
        }
    }

    long long ans = 0;
    for (int val = max_v; val >= 0; --val) {
        if (dp[val] <= W) {
            ans = val;
            break;
        }
    }

    cout << ans << "\n";
    return 0;
}
