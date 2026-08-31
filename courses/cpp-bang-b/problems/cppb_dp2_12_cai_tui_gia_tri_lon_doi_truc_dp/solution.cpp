#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> weight(n), val(n);
    int max_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> weight[i] >> val[i];
        max_v += val[i];
    }

    // Đổi trục: dp[v] = khối lượng nhỏ nhất để đạt được tổng giá trị v
    vector<long long> dp(max_v + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int v = max_v; v >= val[i]; --v) {
            if (dp[v - val[i]] != INF) {
                dp[v] = min(dp[v], dp[v - val[i]] + weight[i]);
            }
        }
    }

    long long ans = 0;
    for (int v = max_v; v >= 0; --v) {
        if (dp[v] <= w) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";
    return 0;
}
