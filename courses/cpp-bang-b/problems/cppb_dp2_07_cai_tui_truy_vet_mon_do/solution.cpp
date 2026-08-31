#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> weight(n + 1), val(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> weight[i] >> val[i];
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(w + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= w; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j >= weight[i]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i]] + val[i]);
            }
        }
    }

    // Truy vết các món đồ được chọn
    vector<int> chosen;
    int curr_w = w;
    for (int i = n; i >= 1; --i) {
        if (curr_w >= weight[i] && dp[i][curr_w] == dp[i - 1][curr_w - weight[i]] + val[i]) {
            chosen.push_back(i);
            curr_w -= weight[i];
        }
    }
    reverse(chosen.begin(), chosen.end());

    cout << dp[n][w] << "\n";
    cout << chosen.size() << "\n";
    for (int i = 0; i < (int)chosen.size(); ++i) {
        cout << chosen[i] << (i + 1 == (int)chosen.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
