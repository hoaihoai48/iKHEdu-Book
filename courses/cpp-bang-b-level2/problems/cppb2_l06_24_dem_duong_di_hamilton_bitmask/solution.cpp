#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;
int dp[1 << 20][20];
vector<int> adj[20];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj[u].push_back(v);
    }

    dp[1][0] = 1; // Bắt đầu từ đỉnh 0 với mask = 1

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (!dp[mask][u]) continue;
            if (u == n - 1 && mask != (1 << n) - 1) continue;

            for (int v : adj[u]) {
                if (!(mask & (1 << v))) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = (dp[next_mask][v] + dp[mask][u]) % MOD;
                }
            }
        }
    }

    cout << dp[(1 << n) - 1][n - 1] << "\n";
    return 0;
}
