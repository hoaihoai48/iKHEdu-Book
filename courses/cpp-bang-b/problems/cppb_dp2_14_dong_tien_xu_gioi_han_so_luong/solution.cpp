#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;
    if (n <= 0 || s < 0) return 0;

    vector<int> dp(s + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        int v, c;
        cin >> v >> c;
        // Phân rã nhị phân số lượng c thành 1, 2, 4, ...
        int k = 1;
        while (c > 0) {
            int take = min(k, c);
            int weight = take * v;
            int coins = take;

            for (int j = s; j >= weight; --j) {
                if (dp[j - weight] != INF) {
                    dp[j] = min(dp[j], dp[j - weight] + coins);
                }
            }

            c -= take;
            k *= 2;
        }
    }

    if (dp[s] == INF) cout << -1 << "\n";
    else cout << dp[s] << "\n";
    return 0;
}
